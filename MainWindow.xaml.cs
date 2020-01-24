using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Diagnostics;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.IO;

namespace TBtoADPcsharp
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        string companycode = "";     

        public MainWindow()
        {
            InitializeComponent();
        }

        private void RadioButton_Checked(object sender, RoutedEventArgs e)
        {
            companycode = "SKY";
        }
        private void TowRadio_Checked(object sender, RoutedEventArgs e)
        {
            companycode = "TOW";
        }

        private void HolidayButton_Click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.DefaultExt = ".csv";
            ofd.Filter = "CSV File (.csv)|*.csv";
            if (ofd.ShowDialog() == true)
            {
                string HolidayFileName = ofd.FileName;
                HolidayFileTextBox.Text = HolidayFileName;
            }
        }

        private void JobCodeButton_Click_1(object sender, RoutedEventArgs e)
        {
            OpenFileDialog ofd2 = new OpenFileDialog();
            ofd2.DefaultExt = ".csv";
            ofd2.Filter = "CSV File (.csv)|*.csv";
            if (ofd2.ShowDialog() == true)
            {
                string JobCodeFileName = ofd2.FileName;
                JobCodeTextBox.Text = JobCodeFileName;
            }
        }

        private void UserExceptionButton_Click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog ofd3 = new OpenFileDialog();
            ofd3.DefaultExt = ".csv";
            ofd3.Filter = "CSV File (.csv)|*.csv";
            if (ofd3.ShowDialog() == true)
            {
                string UserExceptionFileName = ofd3.FileName;
                UserExceptionTextBox.Text = UserExceptionFileName;
            }
        }

        private void OTDetailsButton_click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog ofd4 = new OpenFileDialog();
            ofd4.DefaultExt = ".csv";
            ofd4.Filter = "CSV File (.csv)|*.csv";
            if (ofd4.ShowDialog() == true)
            {
                string OTDetailsFileName = ofd4.FileName;
                OTDetailsTextBox.Text = OTDetailsFileName;
            }
        }

        private void CalculateButton_Click(object sender, RoutedEventArgs e)
        {
            var ThisLocation = System.AppDomain.CurrentDomain.BaseDirectory;
            var ResourceFolder = ThisLocation + @"Resources\";
            if (HolidayFileTextBox.Text != "File")
            {
                System.IO.File.Copy(HolidayFileTextBox.Text, (ResourceFolder + "Holidays.csv"), true);
            }
            if (JobCodeTextBox.Text != "File")
            {
                System.IO.File.Copy(JobCodeTextBox.Text, (ResourceFolder + "JobCodes.csv"), true);
            }
            if (UserExceptionTextBox.Text != "File")
            {
                System.IO.File.Copy(UserExceptionTextBox.Text, (ResourceFolder + "UserExceptions.csv"), true);
            }
            if (OTDetailsTextBox.Text != "File")
            {
                System.IO.File.Copy(OTDetailsTextBox.Text, (ResourceFolder + companycode + "OTDetails.csv"), true);
                Process.Start(ResourceFolder + "script.exe");
            }
        }
    }
}

