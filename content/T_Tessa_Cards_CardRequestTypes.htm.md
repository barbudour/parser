# CardRequestTypes - класс
Типы стандартных запросов к сервису карточек через метод
[RequestAsync(CardRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_RequestAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardRequestTypes
VB __Копировать
     Public NotInheritable Class CardRequestTypes
C++ __Копировать
     public ref class CardRequestTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardRequestTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardRequestTypes
##  __Поля
[ApplyUserSettingsToRoles](F_Tessa_Cards_CardRequestTypes_ApplyUserSettingsToRoles.htm)|
Запрос на копирование настроек одного сотрудника на заданный список ролей (без
учёта заместителей). Запрос доступен только для администраторов.  
---|---  
[ChangePassword](F_Tessa_Cards_CardRequestTypes_ChangePassword.htm)|  Запрос
на изменение пароля для сотрудника с типом входа "Пользователь Tessa".  
[DeleteNotificationSubscription](F_Tessa_Cards_CardRequestTypes_DeleteNotificationSubscription.htm)|
Запрос на удаление списка подписок на уведомление.  
[EditCardInTemplate](F_Tessa_Cards_CardRequestTypes_EditCardInTemplate.htm)|
Запрос на подготовку карточки в шаблоне к редактированию.  
[GetDigest](F_Tessa_Cards_CardRequestTypes_GetDigest.htm)|  Запрос на
получение Digest для сохранения в историю действий с карточкой или для
отображения пользователю в названии вкладки.  
[GetFileSource](F_Tessa_Cards_CardRequestTypes_GetFileSource.htm)|  Запрос на
получение источника, в который сохраняется файл, выполняемый при изменении
контента этого файла. Запрос выполняется только на сервере в расширениях
платформы.  
[GetTypeIDList](F_Tessa_Cards_CardRequestTypes_GetTypeIDList.htm)|  Запрос на
получение типов карточек по списку идентификаторов карточек. Используется,
например, для массового удаления карточек, когда известны только их
идентификаторы.  
[GetVersionSignatures](F_Tessa_Cards_CardRequestTypes_GetVersionSignatures.htm)|
Запрос на загрузку подписей для заданной версии файла.  
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm)|  Запрос
на сброс кэшей.  
[MailSent](F_Tessa_Cards_CardRequestTypes_MailSent.htm)|  Запрос на выполнение
обработки после успешной отправки письма. В этом случае обычно выполняется
очистка, в т.ч. для приложенных файлов, если они формировались динамически. В
объекте [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) содержатся
параметра отправленного письма: MailInfo \- сериализованный объект
[MailInfo](T_Tessa_Notices_MailInfo.htm); Email \- один или несколько почтовых
адресов, на которые было отправлено письмо; Subject \- тема письма; Body \-
тело письма, обычно в формате HTML.  
[MySettingsNotificationPlaceholder](F_Tessa_Cards_CardRequestTypes_MySettingsNotificationPlaceholder.htm)|
Запрос на получение занчений плейсхолдера для вкладки "Уведомления" в "Моих
настройках"  
[RepairConditionTypes](F_Tessa_Cards_CardRequestTypes_RepairConditionTypes.htm)|
Запрос на починку типов условий через
[IConditionRepairManager](T_Tessa_Platform_Conditions_IConditionRepairManager.htm).  
[ResetUserSettings](F_Tessa_Cards_CardRequestTypes_ResetUserSettings.htm)|
Запрос на сброс всех личных настроек пользователя. В параметре
[CardID](P_Tessa_Cards_CardRequest_CardID.htm) содержится идентификатор
сотрудника, для которого выполняется сброс. Обработчик по умолчанию
выполняется только для текущего пользователя или, если пользователь является
администратором, то для любого пользователя.  
[ResolveUserCipherInfo](F_Tessa_Cards_CardRequestTypes_ResolveUserCipherInfo.htm)|
Запрос на получение актуализированной информации по ключам шифрования для
текущего пользователя.  
[SaveCardInTemplate](F_Tessa_Cards_CardRequestTypes_SaveCardInTemplate.htm)|
Запрос на подготовку отредактированной карточки для сохранения в шаблоне.  
[SaveCardModelSettings](F_Tessa_Cards_CardRequestTypes_SaveCardModelSettings.htm)|
Запрос на сохранение настроек текущего сотрудника, связанных с карточками, в
т.ч. с настройками предпросмотра.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
