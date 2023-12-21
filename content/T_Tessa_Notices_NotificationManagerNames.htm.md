# NotificationManagerNames - класс
Имена поставщиков
[INotificationManager](T_Tessa_Notices_INotificationManager.htm),
регистрируемых в Unity.
## __Definition
 **Пространство имён:** [Tessa.Notices](N_Tessa_Notices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class NotificationManagerNames
VB __Копировать
     Public NotInheritable Class NotificationManagerNames
C++ __Копировать
     public ref class NotificationManagerNames abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type NotificationManagerNames = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NotificationManagerNames
##  __Поля
[Default](F_Tessa_Notices_NotificationManagerNames_Default.htm)|  Поставщик
уведомлений по умолчанию, использующий транзакции.  
---|---  
[DeferredWithoutTransaction](F_Tessa_Notices_NotificationManagerNames_DeferredWithoutTransaction.htm)|
Поставщик уведомлений без транзакции и блокировок, который производит
фактический расчет писем и отправку отложенно.  
[WithoutTransaction](F_Tessa_Notices_NotificationManagerNames_WithoutTransaction.htm)|
Поставщик уведомлений без транзакции и блокировок.  
## __См. также
#### Ссылки
[Tessa.Notices - пространство имён](N_Tessa_Notices.htm)
