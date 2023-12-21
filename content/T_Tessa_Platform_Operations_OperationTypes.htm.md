# OperationTypes - класс
Стандартные типы операций.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Operations](N_Tessa_Platform_Operations.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class OperationTypes
VB __Копировать
     Public NotInheritable Class OperationTypes
C++ __Копировать
     public ref class OperationTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type OperationTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ OperationTypes
##  __Свойства
[AdminClientOperations](P_Tessa_Platform_Operations_OperationTypes_AdminClientOperations.htm)|
Операции, создание и управлением которыми доступно со стороны клиента только
для администраторов. Со стороны сервера операции не ограничиваются.  
---|---  
[UserClientOperations](P_Tessa_Platform_Operations_OperationTypes_UserClientOperations.htm)|
Операции, создание и управление которыми доступно со стороны клиента для любых
пользователей, т.е. для администраторов или пользователей без административных
прав. Со стороны сервера операции не ограничиваются.  
## __Поля
[AdSync](F_Tessa_Platform_Operations_OperationTypes_AdSync.htm)|
Синхронизация данных с Active Directory.  
---|---  
[CalendarRebuild](F_Tessa_Platform_Operations_OperationTypes_CalendarRebuild.htm)|
Расчёт календаря.  
[CardImport](F_Tessa_Platform_Operations_OperationTypes_CardImport.htm)|
Потоковый импорт карточки.  
[CardStore](F_Tessa_Platform_Operations_OperationTypes_CardStore.htm)|
Потоковое сохранение карточки.  
[FileConvert](F_Tessa_Platform_Operations_OperationTypes_FileConvert.htm)|
Конвертация файла из одного формата в другой.  
[ForumNewMessagesProcessingNotificationsOperationID](F_Tessa_Platform_Operations_OperationTypes_ForumNewMessagesProcessingNotificationsOperationID.htm)|
Ассинхронная отправка уведомлений по новым сообщениям в форумах  
[Other](F_Tessa_Platform_Operations_OperationTypes_Other.htm)|  Безымянная
операция.  
[WorkflowAsync](F_Tessa_Platform_Operations_OperationTypes_WorkflowAsync.htm)|
Асинхронная обработка WorkflowEngine  
## __См. также
#### Ссылки
[Tessa.Platform.Operations - пространство
имён](N_Tessa_Platform_Operations.htm)
