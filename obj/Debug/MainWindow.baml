   M S B A M L   `   `   `  ����H  DTBtoADPcsharp, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null-clr-namespace:TBtoADPcsharpTBtoADPcsharp  5   	       TBtoADPcsharp.MainWindow   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   -localclr-namespace:TBtoADPcsharp     5   	   -   5          �Name$  MainWindow1��5   	    � Title$0 *Waikiki Business Plaza: TouchBistro to ADP��5   	   $��371.829��6<   $��388.487��6M    � WindowStartupLocation$ CenterOwner=�6]   .��5	      � -   5         �Name$
 Grid��5	      $��0,0,0,0q�6    � RowDefinitions 5
   
   �� 5      $
��Auto �6   �� 5      $
��Auto �6   �� 5      $
��Auto �6   .+�5   
   	� -   5         	�Name$ SkyRadio��5      $��Sky Waikiki��6(   $
��Left=�6>   $��	10,34,0,0q�6Y   $	��Top=�6l    	� 	GroupName$ venue��6�   	� 5   
   -   5        $ TowRadio��5      $��Top of Waikiki��6(   $��100,34,177,0q�6A   $	��Top=�6W   $ venue��6o   6�   �� 5   
   -   5         ��Name$ 
VenueLabel��5      $��Select Venue:��6$   $
��Left=�6<   $��10,8,0,0q�6W   $	��Top=�6i   $
��Bold"�6�   �� 5   
   -   5        $ HolidayLabel��5      $��Select Holiday File:��6&   $
��Left=�6E   $��	10,66,0,0q�6`   $
��Bold"�6s   $��25��6�   $	��Top=�6�   �� 5   
   -   5         ��Name$ HolidayButton��5      $��Browse��6(   $
��Left=�69   $��	10,91,0,0q�6T   $	��Top=�6g   $��75��6   6�   �� 5   
   -   5        	 ��Name$	 HolidayFileTextBox��5      $��20��6.   $��
90,91,23,0q�6:   $
��File��6N   $	��Top=�6Z   
 �� 
IsReadOnly
 . 6r   �� 5   
   -	   5        $ JobCodeLabel��5      $��Select Job Codes File:��6&   $
��Left=�6G   $��
10,130,0,0q�6b   $
��Bold"�6v   $��25��6�   $	��Top=�6�   �� 5   
   -
   5        $ JobCodeButton��5      $��Browse��6(   $
��Left=�69   $��10,156,0,146q�6T   $��76��6j   6�   �� 5   
   -   5        $	 JobCodeTextBox��5      $��91,156,23,146q�6*   $
��File��6A   
 . 6M   �� 5   
   -   5        $ UserEceptionFile��5      $!��Select User Exception File:��6*   $
��Left=�6P   $��
10,196,0,0q�6k   $
��Bold"�6   $��25��6�   $	��Top=�6�   �� 5   
   -   5        $ UserExceptionButton��5      $��Browse��6.   $
��Left=�6?   $��
10,226,0,0q�6Z   $	��Top=�6n   $��75��6�   6�   �� 5   
   -   5        $	 UserExceptionTextBox��5      $
��Left=�60   $��20��6K   $��
91,226,0,0q�6W   $
��File��6k   $	��Top=�6w   $	��264��6�   
 . 6�   �� 5   
   -   5        $ OTDetailsButton��5      $��Browse��6*   $
��Left=�6;   $��
10,301,0,0q�6V   $	��Top=�6j   $��75��6�   6�   �� 5   
   -   5        $ ImportFileLabel��5      $��Select OT Details File:��6)   $
��Left=�6K   $��
10,270,0,0q�6f   $
��Bold"�6z   $��25��6�   $	��Top=�6�   �� 5   
   -   5        $	 OTDetailsTextBox��5      $
��Left=�6,   $��20��6G   $��
91,301,0,0q�6S   $
��File��6g   $	��Top=�6s   $	��264��6�   
 . 6�   �� 5   
   -   5        $ CalculateButton��5      $��	Calculate��6*   $
��Left=�6>   $��
282,19,0,0q�6Y   $	��Top=�6m   $��75��6�   6�   5       5!      