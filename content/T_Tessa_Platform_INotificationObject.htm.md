# INotificationObject - интерфейс
Объект, поддерживающий уведомления об изменениях в своём состоянии.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INotificationObject
VB __Копировать
     Public Interface INotificationObject
C++ __Копировать
     public interface class INotificationObject
F# __Копировать
     type INotificationObject = interface end
##  __Методы
[IsModified](M_Tessa_Platform_INotificationObject_IsModified.htm)| Возвращает
признак того, что объект был изменён с момента его создания.  
---|---  
[SetModified](M_Tessa_Platform_INotificationObject_SetModified.htm)|
Устанавливает признак наличия изменений в значение value. Если изменения
отсутствовали и этот метод установил значение true, то подписчики события
[Modified] уведомляются о наступлении события.  
## __События
[Modified](E_Tessa_Platform_INotificationObject_Modified.htm)|  Событие,
подписчики которого уведомляются в момент первого изменения объекта с момента
его создания. После вызова методов сериализации и установки другого хранилища
признак изменений сбрасывается, поэтому событие возникает повторно.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
