# ActionTypes - класс
Стандартные типы действий в истории
[ActionType](T_Tessa_Platform_Runtime_ActionType.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ActionTypes
VB __Копировать
     Public NotInheritable Class ActionTypes
C++ __Копировать
     public ref class ActionTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ActionTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ActionTypes
##  __Методы
[IsKnown](M_Tessa_Platform_Runtime_ActionTypes_IsKnown.htm)|  Возвращает
признак того, что тип события является известным для стандартного API.  
---|---  
## __Поля
[AcquireNumber](F_Tessa_Platform_Runtime_ActionTypes_AcquireNumber.htm)|
Выделен очередной номер из последовательности без резервирования.
Соответствует методу [AcquireNumberAsync(String, IValidationResultBuilder,
CancellationToken)](M_Tessa_Sequences_ISequenceProvider_AcquireNumberAsync.htm).  
---|---  
[AcquireReservedNumber](F_Tessa_Platform_Runtime_ActionTypes_AcquireReservedNumber.htm)|
Выделен заданный номер из последовательности, который уже был зарезервирован.
Соответствует методу [AcquireReservedNumberAsync(String, Int64,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Sequences_ISequenceProvider_AcquireReservedNumberAsync.htm).  
[AcquireUnreservedNumber](F_Tessa_Platform_Runtime_ActionTypes_AcquireUnreservedNumber.htm)|
Выделен заданный номер из последовательности, который не был зарезервирован.
Соответствует методу [AcquireUnreservedNumberAsync(String, Int64,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Sequences_ISequenceProvider_AcquireUnreservedNumberAsync.htm).  
[AddCardType](F_Tessa_Platform_Runtime_ActionTypes_AddCardType.htm)|
Добавление нового тип карточки.  
[AddView](F_Tessa_Platform_Runtime_ActionTypes_AddView.htm)|  Добавление
представления.  
[AddWorkplace](F_Tessa_Platform_Runtime_ActionTypes_AddWorkplace.htm)|
Добавление рабочего места.  
[All](F_Tessa_Platform_Runtime_ActionTypes_All.htm)|  Список всех типов
действий в истории, которые являются частью стандартного API.  
[Create](F_Tessa_Platform_Runtime_ActionTypes_Create.htm)|  Запрос к методу
[StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_StoreAsync.htm) для создания
карточки.  
[Delete](F_Tessa_Platform_Runtime_ActionTypes_Delete.htm)|  Запрос к методу
[DeleteAsync(CardDeleteRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_DeleteAsync.htm) для
удаления карточки.  
[DeleteCardType](F_Tessa_Platform_Runtime_ActionTypes_DeleteCardType.htm)|
Удаление типа карточки.  
[DeleteFunction](F_Tessa_Platform_Runtime_ActionTypes_DeleteFunction.htm)|
Удаление функции.  
[DeleteLocalizationLibrary](F_Tessa_Platform_Runtime_ActionTypes_DeleteLocalizationLibrary.htm)|
Удаление библиотеки локализации.  
[DeleteMigration](F_Tessa_Platform_Runtime_ActionTypes_DeleteMigration.htm)|
Удаление миграции.  
[DeletePartition](F_Tessa_Platform_Runtime_ActionTypes_DeletePartition.htm)|
Удаление библиотеки.  
[DeleteProcedure](F_Tessa_Platform_Runtime_ActionTypes_DeleteProcedure.htm)|
Удаление процедуры.  
[DeleteTable](F_Tessa_Platform_Runtime_ActionTypes_DeleteTable.htm)|  Удаление
таблицы.  
[DeleteView](F_Tessa_Platform_Runtime_ActionTypes_DeleteView.htm)|  Удаление
представления.  
[DeleteWorkplace](F_Tessa_Platform_Runtime_ActionTypes_DeleteWorkplace.htm)|
Удаление рабочего места.  
[DereserveNumber](F_Tessa_Platform_Runtime_ActionTypes_DereserveNumber.htm)|
Дерезервирован номер из последовательности, который был зарезервирован.
Соответствует методу [DereserveNumberAsync(String, Int64,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Sequences_ISequenceProvider_DereserveNumberAsync.htm).  
[Error](F_Tessa_Platform_Runtime_ActionTypes_Error.htm)|  Ошибка с
произвольным описанием.  
[Export](F_Tessa_Platform_Runtime_ActionTypes_Export.htm)|  Запрос к методу
[GetAsync(CardGetRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_GetAsync.htm) для
административного экспорта карточки.  
[FinalDelete](F_Tessa_Platform_Runtime_ActionTypes_FinalDelete.htm)|  Запрос к
методу [DeleteAsync(CardDeleteRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_DeleteAsync.htm) для
удаления карточки [DeletedTypeID](F_Tessa_Cards_CardHelper_DeletedTypeID.htm)
из корзины.  
[Get](F_Tessa_Platform_Runtime_ActionTypes_Get.htm)|  Запрос к методу
[GetAsync(CardGetRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_GetAsync.htm) для открытия
карточки.  
[GetFile](F_Tessa_Platform_Runtime_ActionTypes_GetFile.htm)|  Запрос к методам
[GetFileContentAsync(CardGetFileContentRequest, Func<Stream,
CancellationToken, ValueTask>, Func<CardGetFileContentResponse,
CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Cards_ICardStreamClientRepository_GetFileContentAsync.htm)
или [GetFileContentAsync(CardGetFileContentRequest,
CancellationToken)](M_Tessa_Cards_ICardStreamServerRepository_GetFileContentAsync.htm)
для открытия контента файла.  
[Import](F_Tessa_Platform_Runtime_ActionTypes_Import.htm)|  Запрос к методу
[StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_StoreAsync.htm) для
административного импорта карточки.  
[ImportView](F_Tessa_Platform_Runtime_ActionTypes_ImportView.htm)|  Импорт
представления.  
[ImportWorkplace](F_Tessa_Platform_Runtime_ActionTypes_ImportWorkplace.htm)|
Импорт рабочего места.  
[Login](F_Tessa_Platform_Runtime_ActionTypes_Login.htm)|  Пользователь
выполнил вход в систему.  
[LoginFailed](F_Tessa_Platform_Runtime_ActionTypes_LoginFailed.htm)|  Попытка
входа в систему выполнена неудачно. Логин или пароль введены некорректно.  
[Logout](F_Tessa_Platform_Runtime_ActionTypes_Logout.htm)|  Пользователь
корректно вышел из системы (т.е. сессия была завершена в результате выхода из
приложения, а не в результате разрыва соединения и других неполадок).  
[Modify](F_Tessa_Platform_Runtime_ActionTypes_Modify.htm)|  Запрос к методу
[StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_StoreAsync.htm) для
изменения карточки.  
[ModifyCardType](F_Tessa_Platform_Runtime_ActionTypes_ModifyCardType.htm)|
Обновление типа карточки.  
[ModifyFunction](F_Tessa_Platform_Runtime_ActionTypes_ModifyFunction.htm)|
Сохранение функции.  
[ModifyLocalizationLibrary](F_Tessa_Platform_Runtime_ActionTypes_ModifyLocalizationLibrary.htm)|
Добавление библиотеки локализации.  
[ModifyMigration](F_Tessa_Platform_Runtime_ActionTypes_ModifyMigration.htm)|
Сохранение миграции.  
[ModifyPartition](F_Tessa_Platform_Runtime_ActionTypes_ModifyPartition.htm)|
Сохранение библиотеки.  
[ModifyProcedure](F_Tessa_Platform_Runtime_ActionTypes_ModifyProcedure.htm)|
Сохранение процедуры.  
[ModifyTable](F_Tessa_Platform_Runtime_ActionTypes_ModifyTable.htm)|
Сохранение таблицы.  
[ModifyView](F_Tessa_Platform_Runtime_ActionTypes_ModifyView.htm)|  Обновление
представления.  
[ModifyWorkplace](F_Tessa_Platform_Runtime_ActionTypes_ModifyWorkplace.htm)|
Обновление рабочего места.  
[ReleaseNumber](F_Tessa_Platform_Runtime_ActionTypes_ReleaseNumber.htm)|
Освобождён номер из последовательности, который был выделен. Соответствует
методу [ReleaseNumberAsync(String, Int64, IValidationResultBuilder,
CancellationToken)](M_Tessa_Sequences_ISequenceProvider_ReleaseNumberAsync.htm).  
[ReserveAcquiredNumber](F_Tessa_Platform_Runtime_ActionTypes_ReserveAcquiredNumber.htm)|
Зарезервирован заданный номер из последовательности, который ранее мог быть
выделен. Соответствует методу [ReserveAcquiredNumberAsync(String, Int64,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Sequences_ISequenceProvider_ReserveAcquiredNumberAsync.htm).  
[ReserveNumber](F_Tessa_Platform_Runtime_ActionTypes_ReserveNumber.htm)|
Зарезервирован очередной номер из последовательности. Соответствует методу
[ReserveNumberAsync(String, IValidationResultBuilder,
CancellationToken)](M_Tessa_Sequences_ISequenceProvider_ReserveNumberAsync.htm).  
[Restore](F_Tessa_Platform_Runtime_ActionTypes_Restore.htm)|  Запрос к методу
[StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_StoreAsync.htm) для
восстановления удалённой карточки.  
[SessionClosedByAdmin](F_Tessa_Platform_Runtime_ActionTypes_SessionClosedByAdmin.htm)|
Сессия закрыта администратором.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
