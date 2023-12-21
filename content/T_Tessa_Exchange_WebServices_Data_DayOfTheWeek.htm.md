# DayOfTheWeek - перечисление
Specifies the day of the week.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum DayOfTheWeek
VB __Копировать
     Public Enumeration DayOfTheWeek
C++ __Копировать
     public enum class DayOfTheWeek
F# __Копировать
     type DayOfTheWeek
##  __Заметки
For the standard days of the week (Sunday, Monday...) the DayOfTheWeek enum
value is the same as the System.DayOfWeek enum type. These values can be
safely cast between the two enum types. The special days of the week (Day,
Weekday and WeekendDay) are used for monthly and yearly recurrences and cannot
be cast to System.DayOfWeek values.
## __Члены
Sunday| 0|  Sunday  
---|---|---  
Monday| 1|  Monday  
Tuesday| 2|  Tuesday  
Wednesday| 3|  Wednesday  
Thursday| 4|  Thursday  
Friday| 5|  Friday  
Saturday| 6|  Saturday  
Day| 7|  Any day of the week  
Weekday| 8|  Any day of the usual business week (Monday-Friday)  
WeekendDay| 9|  Any weekend day (Saturday or Sunday)  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
