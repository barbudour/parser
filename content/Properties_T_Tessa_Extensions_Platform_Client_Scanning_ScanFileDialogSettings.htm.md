# ScanFileDialogSettings - свойства
##  __Свойства
[CancellationToken](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardMetadata](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_CardMetadata.htm)|
Метаинформация по карточкам. Не равна null.  
[Context](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_Context.htm)|
Контекст расширений, из которого было инициировано открытие диалога
сканирования. Не может быть равен null.  
[DialogCaption](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_DialogCaption.htm)|
Заголовок диалогового окна.  
[DialogService](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_DialogService.htm)|
Сервис диалогов. Не равен null.  
[DocumentTypeFilterFunc](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_DocumentTypeFilterFunc.htm)|
Функция, получающая тип документа и возвращающая признак того, что этот тип
документа доступен для выбора.  
[DocumentTypesOverride](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_DocumentTypesOverride.htm)|
Настройка, позволяющая переопределить типы генерируемых документов по
умолчанию на заданный список типов. Если значение равно null (по умолчанию),
то используется список типов по умолчанию
[DefaultTypes](P_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType_DefaultTypes.htm).  
[FileToReplace](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_FileToReplace.htm)|
Файл, который будет заменён при сохранении документа, или null, если будет
создан новый файл.  
[ForceIsDirty](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_ForceIsDirty.htm)|
Признак того, что диалог будет открыт как
[IsDirty](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_IsDirty.htm).  
[HideDocumentTypeSelection](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_HideDocumentTypeSelection.htm)|
Признак того, что выбор типа документа должен быть недоступен для
пользователя.  
[InitialDocumentType](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_InitialDocumentType.htm)|
Выбранный тип документа, для которого будет выполнена генерация при сохранении
документа, или null, если тип определяется автоматически.  
[MenuActionName](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_MenuActionName.htm)|
Имя действия из меню
[FileMenuActionNames](T_Tessa_UI_Files_FileMenuActionNames.htm), в рамках
которого открывается диалог, или null, если действие неизвестно.  
[ModifyDialogActionAsync](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_ModifyDialogActionAsync.htm)|
Метод, который получает модель представления диалога
[ScanDialogViewModel](T_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel.htm),
после чего может как угодно его изменить.  
[NotificationUIManager](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_NotificationUIManager.htm)|
Сервис отображения всплывающих уведомлений. Не равен null.  
[Session](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_Session.htm)|
Сессия текущего пользователя. Не равна null.  
[UnityContainer](P_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_UnityContainer.htm)|
Контейнер Unity, из которого расширения могут получать сервисы и объекты. Не
равен null.  
## __См. также
#### Ссылки
[ScanFileDialogSettings -
](T_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
