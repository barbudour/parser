# ScanFileDialogSettings - класс
Настройки диалога сканирования или диалога редактирования изображений.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ScanFileDialogSettings : IExtensionContext
VB __Копировать
     Public NotInheritable Class ScanFileDialogSettings
    	Implements IExtensionContext
C++ __Копировать
     public ref class ScanFileDialogSettings sealed : IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type ScanFileDialogSettings = 
        class
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ScanFileDialogSettings
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[ScanFileDialogSettings](M_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings__ctor.htm)|
Инициализирует новый экземпляр класса ScanFileDialogSettings  
---|---  
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
## __Методы
[CreateScanProvider](M_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_CreateScanProvider.htm)|
Создаёт объект провайдера, обеспечивающий сканирование.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetInitialDocumentTypeAccordingToLastUsed](M_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings_SetInitialDocumentTypeAccordingToLastUsed.htm)|
Устанавливает в качестве типа по умолчанию последний используемый тип
документа или заданный documentType, если последний используемый отсутствует.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
