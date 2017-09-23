using Android.App;
using Android.Widget;
using Android.OS;
using Android.Bluetooth;
using System;
using System.Linq;
using Java.Util;
using System.Text;

namespace PiBot
{
    [Activity(Label = "PiBot", MainLauncher = true, Icon = "@mipmap/icon")]
    public class MainActivity : Activity
    {
        BluetoothDevice device;
        BluetoothAdapter adapter;
        Button btnConnect;
        Button btnLeft;
        Button btnRight;
        Button btnForward;
        Button btnReverse;
        Button btnStop;
        TextView txtStatus;
        BluetoothSocket socket;
        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            SetContentView(Resource.Layout.Main);
            btnConnect = this.FindViewById<Button>(Resource.Id.btnConnect);
            btnLeft = this.FindViewById<Button>(Resource.Id.btnLeft);
            btnRight = this.FindViewById<Button>(Resource.Id.btnRight);
            btnForward = this.FindViewById<Button>(Resource.Id.btnForward);
            btnReverse = this.FindViewById<Button>(Resource.Id.btnReverse);
            btnStop = this.FindViewById<Button>(Resource.Id.btnStop);
            txtStatus = this.FindViewById<TextView>(Resource.Id.txtStatus);
            btnConnect.Click += BtnConnect_Click;
            btnLeft.Click += BtnLeft_Click;
            btnRight.Click += BtnRight_Click;
            btnStop.Click += BtnStop_Click;
            btnForward.Click += BtnForward_Click;
            btnReverse.Click += BtnReverse_Click;
            EnableOrDisableAllMainFunctions(false);
        }

        private void EnableOrDisableAllMainFunctions(bool isEnabled){
            btnLeft.Enabled = btnRight.Enabled = btnForward.Enabled = btnReverse.Enabled = btnStop.Enabled = isEnabled;
        }

        async void BtnConnect_Click(object sender, EventArgs e)
        {
            try
            {
                adapter = BluetoothAdapter.DefaultAdapter;
                if (adapter == null)
                    throw new Exception("No Bluetooth adapter found.");

                if (!adapter.IsEnabled)
                    throw new Exception("Bluetooth adapter is not enabled.");

                device = (from bd in adapter.BondedDevices
                          where bd.Name == "raspberrypi"
                          select bd).FirstOrDefault();

                if (device == null)
                    throw new Exception("Raspberry Pi device not found.");

                socket = device.CreateRfcommSocketToServiceRecord(UUID.FromString("00001101-0000-1000-8000-00805f9b34fb"));
                await socket.ConnectAsync();
                txtStatus.Text = "Pi Robot Connected";
                EnableOrDisableAllMainFunctions(true);
                btnConnect.Enabled = false;
            }
            catch (Exception ex)
            {
                txtStatus.Text = ex.Message;
                Toast.MakeText(this, ex.Message, ToastLength.Short);
            }
        }
        void BtnReverse_Click(object sender, EventArgs e)
        {
            RobotMainFunction("2");
        }

        void BtnForward_Click(object sender, EventArgs e)
        {
            RobotMainFunction("1");
        }

        void BtnStop_Click(object sender, EventArgs e)
        {
            RobotMainFunction("0");
        }

        void BtnRight_Click(object sender, EventArgs e)
        {
            RobotMainFunction("4");
        }

        void BtnLeft_Click(object sender, EventArgs e)
        {
            RobotMainFunction("3");
        }
        private async void RobotMainFunction(string strDirection)
        {
            try
            {
                byte[] buffer = Encoding.ASCII.GetBytes(strDirection);
                await socket.OutputStream.WriteAsync(buffer, 0, buffer.Length);
            }
            catch (Exception ex)
            {
                Toast.MakeText(this, ex.Message, ToastLength.Short);
            }
        }
    }
}

