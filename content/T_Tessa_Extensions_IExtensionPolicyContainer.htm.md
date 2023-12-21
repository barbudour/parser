# IExtensionPolicyContainer - интерфейс
Контейнер политик [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm),
ассоциированных с расширениями. Все методы объекта являются потокобезопасными.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IExtensionPolicyContainer
VB __Копировать
     Public Interface IExtensionPolicyContainer
C++ __Копировать
     public interface class IExtensionPolicyContainer
F# __Копировать
     type IExtensionPolicyContainer = interface end
##  __Методы
[Clone](M_Tessa_Extensions_IExtensionPolicyContainer_Clone.htm)| Создаёт
полную копию объекта.  
---|---  
[IsRegistered<TPolicy>](M_Tessa_Extensions_IExtensionPolicyContainer_IsRegistered__1.htm)|
Возвращает признак того, что политика для заданного типа была зарегистрирована
в контейнере.  
[Register](M_Tessa_Extensions_IExtensionPolicyContainer_Register.htm)|
Регистрирует заданную политику, которую можно будет получить по всем типам её
интерфейсов, кроме [Tessa.Extensions.IExtensionPolicy].  
[Resolve<TPolicy>](M_Tessa_Extensions_IExtensionPolicyContainer_Resolve__1.htm)|
Возвращает политику заданного типа, зарегистрированную в контейнере. Если для
типа зарегистрировано несколько политик, то возвращается последняя.  
[ResolveAll<TPolicy>](M_Tessa_Extensions_IExtensionPolicyContainer_ResolveAll__1.htm)|
Возвращает все политики заданного типа, зарегистрированные в контейнере. Если
для типа не зарегистрировано политик, то возвращается пустое перечисление.  
[TryResolve<TPolicy>](M_Tessa_Extensions_IExtensionPolicyContainer_TryResolve__1.htm)|
Возвращает политику заданного типа, зарегистрированную в контейнере, или null,
если политика не была зарегистрирована. Если для типа зарегистрировано
несколько политик, то возвращается последняя.  
## __Методы расширения
[WhenAnyApplication](M_Tessa_Platform_Runtime_RuntimeExtensions_WhenAnyApplication.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым типам
приложений. Используйте для замещения политики, назначенной посредством метода
[WhenApplications(IExtensionPolicyContainer,
Guid[])](M_Tessa_Platform_Runtime_RuntimeExtensions_WhenApplications.htm). Для
того, чтобы политика использовалась, требуется зарегистрировать политику
[ApplicationExtensionFilterPolicy](T_Tessa_Platform_Runtime_ApplicationExtensionFilterPolicy.htm).  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
---|---  
[WhenAnyCardType](M_Tessa_Cards_CardExtensions_WhenAnyCardType.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым типам
карточек. Используйте для замещения политики, назначенной посредством методов
[WhenCardTypes(IExtensionPolicyContainer,
String[])](M_Tessa_Cards_CardExtensions_WhenCardTypes_1.htm) и
[WhenCardTypes(IExtensionPolicyContainer,
Guid[])](M_Tessa_Cards_CardExtensions_WhenCardTypes.htm). Если идентификатор и
имя типа карточки неизвестны, то метод расширения не выполняется. Для того,
чтобы политика использовалась, требуется зарегистрировать политику
[CardTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTypeFilterPolicy.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenAnyDeleteMethod](M_Tessa_Cards_CardExtensions_WhenAnyDeleteMethod.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
методам удаления карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenAnyDialog](M_Tessa_UI_Cards_CardUIExtensions_WhenAnyDialog.htm)|
Регистрирует политику фильтрации выполнения методов расширений для любого
диалога. Для карточек в основном окне расширения выполняться не будут. Для
того, чтобы политика использовалась, требуется зарегистрировать политику
[DialogFilterPolicy](T_Tessa_UI_Cards_DialogFilterPolicy.htm).  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[WhenAnyFileConverterEventName](M_Tessa_FileConverters_FileConverterExtensions_WhenAnyFileConverterEventName.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым именам
событий конвертирования файлов. Используйте для замещения политики,
назначенной посредством метода
[WhenFileConverterEventNames(IExtensionPolicyContainer,
String[])](M_Tessa_FileConverters_FileConverterExtensions_WhenFileConverterEventNames.htm).
Для того, чтобы политика использовалась, требуется зарегистрировать политику
[FileConverterExtensionFilterPolicy](T_Tessa_FileConverters_FileConverterExtensionFilterPolicy.htm).  
(Определяется
[FileConverterExtensions](T_Tessa_FileConverters_FileConverterExtensions.htm))  
[WhenAnyFileConverterOutputFormat](M_Tessa_FileConverters_FileConverterExtensions_WhenAnyFileConverterOutputFormat.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
выходным форматам конвертирования файлов. Используйте для замещения политики,
назначенной посредством метода
[WhenFileConverterOutputFormats(IExtensionPolicyContainer,
FileConverterFormat[])](M_Tessa_FileConverters_FileConverterExtensions_WhenFileConverterOutputFormats.htm).
Для того, чтобы политика использовалась, требуется зарегистрировать политику
[FileConverterExtensionFilterPolicy](T_Tessa_FileConverters_FileConverterExtensionFilterPolicy.htm).  
(Определяется
[FileConverterExtensions](T_Tessa_FileConverters_FileConverterExtensions.htm))  
[WhenAnyFileType](M_Tessa_Cards_CardExtensions_WhenAnyFileType.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым типам
файлов. Используйте для замещения политики, назначенной посредством методов
[WhenFileTypes(IExtensionPolicyContainer,
String[])](M_Tessa_Cards_CardExtensions_WhenFileTypes_1.htm) и
[WhenFileTypes(IExtensionPolicyContainer,
Guid[])](M_Tessa_Cards_CardExtensions_WhenFileTypes.htm). Если идентификатор и
имя типа файла неизвестны, то метод расширения выполняется. Для того, чтобы
политика использовалась, требуется зарегистрировать политику
[CardFileTypeFilterPolicy](T_Tessa_Cards_Extensions_CardFileTypeFilterPolicy.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenAnyGetFileContentMethod](M_Tessa_Cards_CardExtensions_WhenAnyGetFileContentMethod.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
методам загрузки контента файла.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenAnyGetFileVersionsMethod](M_Tessa_Cards_CardExtensions_WhenAnyGetFileVersionsMethod.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
методам загрузки списка версий файла.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenAnyGetMethod](M_Tessa_Cards_CardExtensions_WhenAnyGetMethod.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
методам загрузки карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenAnyNewMethod](M_Tessa_Cards_CardExtensions_WhenAnyNewMethod.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
методам создания карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenAnyRequestType](M_Tessa_Cards_CardExtensions_WhenAnyRequestType.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым именам
универсальных запросов к сервису карточек. Используйте для замещения политики,
назначенной посредством метода [WhenRequestTypes(IExtensionPolicyContainer,
Guid[])](M_Tessa_Cards_CardExtensions_WhenRequestTypes.htm). Имя запроса
является обязательным параметром и должно быть известно. Для того, чтобы
политика использовалась, требуется зарегистрировать политику
[CardRequestFilterPolicy](T_Tessa_Cards_Extensions_CardRequestFilterPolicy.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenAnyStoreMethod](M_Tessa_Cards_CardExtensions_WhenAnyStoreMethod.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
методам сохранения карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenAnyTaskType](M_Tessa_Cards_CardExtensions_WhenAnyTaskType.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым типам
заданий. Используйте для замещения политики, назначенной посредством методов
[WhenTaskTypes(IExtensionPolicyContainer,
String[])](M_Tessa_Cards_CardExtensions_WhenTaskTypes_1.htm) и
[WhenTaskTypes(IExtensionPolicyContainer,
Guid[])](M_Tessa_Cards_CardExtensions_WhenTaskTypes.htm). Если идентификатор и
имя типа задания неизвестны, то метод расширения выполняется. Для того, чтобы
политика использовалась, требуется зарегистрировать политику
[CardTaskTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTaskTypeFilterPolicy.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenAnyTilePanel](M_Tessa_UI_Tiles_TileExtensions_WhenAnyTilePanel.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любому
местоположению боковой панели. Используйте для замещения политики, назначенной
посредством метода [WhenTilePanel(IExtensionPolicyContainer,
TilePanelLocation)](M_Tessa_UI_Tiles_TileExtensions_WhenTilePanel.htm). Для
того, чтобы политика использовалась, требуется зарегистрировать политику
[TilePanelFilterPolicy](T_Tessa_UI_Tiles_Extensions_TilePanelFilterPolicy.htm).  
(Определяется [TileExtensions](T_Tessa_UI_Tiles_TileExtensions.htm))  
[WhenApplicationFunc](M_Tessa_Platform_Runtime_RuntimeExtensions_WhenApplicationFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IApplicationExtension](T_Tessa_Platform_Runtime_IApplicationExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[WhenApplications](M_Tessa_Platform_Runtime_RuntimeExtensions_WhenApplications.htm)|
Регистрирует политику фильтрации выполнения методов расширений по
идентификатору типа приложения, который входит в заданный список
идентификаторов. Для того, чтобы политика использовалась, требуется
зарегистрировать политику
[ApplicationExtensionFilterPolicy](T_Tessa_Platform_Runtime_ApplicationExtensionFilterPolicy.htm).
Регистрация добавляет значение к списку приложений, а не переопределяет его.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[WhenCardDeleteFunc](M_Tessa_Cards_CardExtensions_WhenCardDeleteFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardDeleteExtension](T_Tessa_Cards_Extensions_ICardDeleteExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenCardGetFileContentFunc](M_Tessa_Cards_CardExtensions_WhenCardGetFileContentFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardGetFileContentExtension](T_Tessa_Cards_Extensions_ICardGetFileContentExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenCardGetFileVersionsFunc](M_Tessa_Cards_CardExtensions_WhenCardGetFileVersionsFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardGetFileVersionsExtension](T_Tessa_Cards_Extensions_ICardGetFileVersionsExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenCardGetFunc](M_Tessa_Cards_CardExtensions_WhenCardGetFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardGetExtension](T_Tessa_Cards_Extensions_ICardGetExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenCardMetadataFunc](M_Tessa_Cards_CardExtensions_WhenCardMetadataFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardMetadataExtension](T_Tessa_Cards_Extensions_ICardMetadataExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenCardNewFunc](M_Tessa_Cards_CardExtensions_WhenCardNewFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardNewExtension](T_Tessa_Cards_Extensions_ICardNewExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenCardRepairFunc](M_Tessa_Cards_CardExtensions_WhenCardRepairFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardRepairExtension](T_Tessa_Cards_Extensions_ICardRepairExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenCardRequestFunc](M_Tessa_Cards_CardExtensions_WhenCardRequestFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenCardStoreFunc](M_Tessa_Cards_CardExtensions_WhenCardStoreFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardStoreExtension](T_Tessa_Cards_Extensions_ICardStoreExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenCardStoreTaskFunc](M_Tessa_Cards_CardExtensions_WhenCardStoreTaskFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardStoreTaskExtension](T_Tessa_Cards_Extensions_ICardStoreTaskExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenCardTypes](M_Tessa_Cards_CardExtensions_WhenCardTypes.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по идентификатору типа
карточки, который входит в заданный список идентификаторов. Если тип карточки
неизвестен, то метод расширения не выполняется. Для того, чтобы политика
использовалась, требуется зарегистрировать политику
[CardTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTypeFilterPolicy.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenCardTypes](M_Tessa_Cards_CardExtensions_WhenCardTypes_1.htm)|
Регистрирует политику фильтрации выполнения методов расширений по имени типа
карточки, которое входит в заданный список имён. Если тип карточки неизвестен,
то метод расширения не выполняется. Для того, чтобы политика использовалась,
требуется зарегистрировать политику
[CardTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTypeFilterPolicy.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenCardUIFunc](M_Tessa_UI_Cards_CardUIExtensions_WhenCardUIFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardUIExtension](T_Tessa_UI_Cards_ICardUIExtension.htm) в соответствии с
функцией isAllowedFunc, которая проверяет контекст расширений. Если
зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[WhenClientInitializationFunc](M_Tessa_Platform_Initialization_InitializationExtensions_WhenClientInitializationFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IClientInitializationExtension](T_Tessa_Platform_Initialization_IClientInitializationExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
(Определяется
[InitializationExtensions](T_Tessa_Platform_Initialization_InitializationExtensions.htm))  
[WhenDefaultDialog](M_Tessa_UI_Cards_CardUIExtensions_WhenDefaultDialog.htm)|
Регистрирует политику фильтрации выполнения методов расширений только для
карточек в основном окне. Для карточек в диалогах расширения выполняться не
будут. Для того, чтобы политика использовалась, требуется зарегистрировать
политику [DialogFilterPolicy](T_Tessa_UI_Cards_DialogFilterPolicy.htm).  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[WhenDialog](M_Tessa_UI_Cards_CardUIExtensions_WhenDialog.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по названию диалога, который
входит в заданный список имен диалогов. Для того, чтобы политика
использовалась, требуется зарегистрировать политику
[DialogFilterPolicy](T_Tessa_UI_Cards_DialogFilterPolicy.htm).  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[WhenEventType](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensions_WhenEventType.htm)|  
(Определяется
[KrEventExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensions.htm))  
[WhenFileControlFunc](M_Tessa_UI_Files_FileUIExtensions_WhenFileControlFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IFileControlExtension](T_Tessa_UI_Files_IFileControlExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [FileUIExtensions](T_Tessa_UI_Files_FileUIExtensions.htm))  
[WhenFileConverterEventNames](M_Tessa_FileConverters_FileConverterExtensions_WhenFileConverterEventNames.htm)|
Регистрирует политику фильтрации выполнения методов расширений по имени
события конвертирования файлов, которое входит в заданный список имён. Для
того, чтобы политика использовалась, требуется зарегистрировать политику
[FileConverterExtensionFilterPolicy](T_Tessa_FileConverters_FileConverterExtensionFilterPolicy.htm).  
(Определяется
[FileConverterExtensions](T_Tessa_FileConverters_FileConverterExtensions.htm))  
[WhenFileConverterFunc](M_Tessa_FileConverters_FileConverterExtensions_WhenFileConverterFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IFileConverterExtension](T_Tessa_FileConverters_IFileConverterExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
(Определяется
[FileConverterExtensions](T_Tessa_FileConverters_FileConverterExtensions.htm))  
[WhenFileConverterOutputFormats](M_Tessa_FileConverters_FileConverterExtensions_WhenFileConverterOutputFormats.htm)|
Регистрирует политику фильтрации выполнения методов расширений по выходному
формату конвертирования файлов, который входит в заданный список форматов. Для
того, чтобы политика использовалась, требуется зарегистрировать политику
[FileConverterExtensionFilterPolicy](T_Tessa_FileConverters_FileConverterExtensionFilterPolicy.htm).  
(Определяется
[FileConverterExtensions](T_Tessa_FileConverters_FileConverterExtensions.htm))  
[WhenFileFunc](M_Tessa_UI_Files_FileUIExtensions_WhenFileFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IFileExtension](T_Tessa_UI_Files_IFileExtension.htm) в соответствии с
функцией isAllowedFunc, которая проверяет контекст расширений. Если
зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [FileUIExtensions](T_Tessa_UI_Files_FileUIExtensions.htm))  
[WhenFileTypes](M_Tessa_Cards_CardExtensions_WhenFileTypes.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по идентификатору типа
файла, который входит в заданный список идентификаторов. Если тип файла
неизвестен, то метод расширения не выполняется. Для того, чтобы политика
использовалась, требуется зарегистрировать политику
[CardFileTypeFilterPolicy](T_Tessa_Cards_Extensions_CardFileTypeFilterPolicy.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenFileTypes](M_Tessa_Cards_CardExtensions_WhenFileTypes_1.htm)|
Регистрирует политику фильтрации выполнения методов расширений по имени типа
файла, которое входит в заданный список имён. Если тип файла неизвестен, то
метод расширения не выполняется. Для того, чтобы политика использовалась,
требуется зарегистрировать политику
[CardFileTypeFilterPolicy](T_Tessa_Cards_Extensions_CardFileTypeFilterPolicy.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenFileVersionFunc](M_Tessa_UI_Files_FileUIExtensions_WhenFileVersionFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IFileVersionExtension](T_Tessa_UI_Files_IFileVersionExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [FileUIExtensions](T_Tessa_UI_Files_FileUIExtensions.htm))  
[WhenFormUIFunc](M_Tessa_UI_UIExtensions_WhenFormUIFunc.htm)|  Регистрирует
политику фильтрации выполнения методов расширений
[IFormUIExtension](T_Tessa_UI_IFormUIExtension.htm) в соответствии с функцией
isAllowedFunc, которая проверяет контекст расширений. Если зарегистрировано
несколько политик, то должны выполняться все из них.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[WhenFunc](M_Tessa_Extensions_ExtensionExtensions_WhenFunc.htm)|  Регистрирует
политику фильтрации выполнения методов любых расширений
[IExtension](T_Tessa_Extensions_IExtension.htm) в соответствии с функцией
isAllowedFunc, которая проверяет контекст расширений. Если зарегистрировано
несколько политик, то должны выполняться все из них.  
(Определяется
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm))  
[WhenFunc<TContext>](M_Tessa_Extensions_ExtensionExtensions_WhenFunc__1.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IExtension](T_Tessa_Extensions_IExtension.htm), принимающих указанный тип
контекста TContext, в соответствии с функцией isAllowedFunc, которая проверяет
контекст расширений. Если зарегистрировано несколько политик, то должны
выполняться все из них. Если тип контекста отличается от указанного, то
политика игнорируется, т.е. возвращает true.  
(Определяется
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm))  
[WhenMethod](M_Tessa_Cards_CardExtensions_WhenMethod.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по списку допустимых методов
удаления карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenMethod](M_Tessa_Cards_CardExtensions_WhenMethod_1.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по списку допустимых методов
загрузки контента файла.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenMethod](M_Tessa_Cards_CardExtensions_WhenMethod_2.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по списку допустимых методов
загрузки списка версий файла.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenMethod](M_Tessa_Cards_CardExtensions_WhenMethod_3.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по списку допустимых методов
загрузки карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenMethod](M_Tessa_Cards_CardExtensions_WhenMethod_4.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по списку допустимых методов
создания карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenMethod](M_Tessa_Cards_CardExtensions_WhenMethod_5.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по списку допустимых методов
сохранения карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenMySettingsFunc](M_Tessa_UI_Cards_CardUIExtensions_WhenMySettingsFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IMySettingsExtension](T_Tessa_UI_Cards_IMySettingsExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[WhenNoDialog](M_Tessa_UI_Cards_CardUIExtensions_WhenNoDialog.htm)|
Регистрирует политику фильтрации выполнения методов расширений только для
карточек в основном окне. Для карточек в диалогах расширения выполняться не
будут. Для того, чтобы политика использовалась, требуется зарегистрировать
политику [DialogFilterPolicy](T_Tessa_UI_Cards_DialogFilterPolicy.htm).  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[WhenPdfStampFunc](M_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensions_WhenPdfStampFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IPdfStampExtension](T_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
(Определяется
[PdfStampExtensions](T_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensions.htm))  
[WhenRequestTypes](M_Tessa_Cards_CardExtensions_WhenRequestTypes.htm)|
Регистрирует политику фильтрации выполнения методов расширений по типу
универсального запроса к сервису карточек, которое входит в заданный список
типов. Тип запроса является обязательным параметром и должен быть известен.
Для того, чтобы политика использовалась, требуется зарегистрировать политику
[CardRequestFilterPolicy](T_Tessa_Cards_Extensions_CardRequestFilterPolicy.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenRouteCardTypes](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtensions_WhenRouteCardTypes.htm)|  
(Определяется
[KrStageRowExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtensions.htm))  
[WhenScanDialogFunc](M_Tessa_Extensions_Platform_Client_Scanning_ScanningExtensions_WhenScanDialogFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IScanDialogExtension](T_Tessa_Extensions_Platform_Client_Scanning_IScanDialogExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
(Определяется
[ScanningExtensions](T_Tessa_Extensions_Platform_Client_Scanning_ScanningExtensions.htm))  
[WhenServerInitializationFunc](M_Tessa_Platform_Initialization_InitializationExtensions_WhenServerInitializationFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IServerInitializationExtension](T_Tessa_Platform_Initialization_IServerInitializationExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
(Определяется
[InitializationExtensions](T_Tessa_Platform_Initialization_InitializationExtensions.htm))  
[WhenSettingsFunc](M_Tessa_Platform_Settings_SettingsExtensions_WhenSettingsFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ISettingsExtension](T_Tessa_Platform_Settings_ISettingsExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется
[SettingsExtensions](T_Tessa_Platform_Settings_SettingsExtensions.htm))  
[WhenTaskTypes](M_Tessa_Cards_CardExtensions_WhenTaskTypes.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по идентификатору типа
задания, который входит в заданный список идентификаторов. Если тип задания
неизвестен, то метод расширения не выполняется. Для того, чтобы политика
использовалась, требуется зарегистрировать политику
[CardTaskTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTaskTypeFilterPolicy.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenTaskTypes](M_Tessa_Cards_CardExtensions_WhenTaskTypes_1.htm)|
Регистрирует политику фильтрации выполнения методов расширений по имени типа
задания, которое входит в заданный список имён. Если тип задания неизвестен,
то метод расширения не выполняется. Для того, чтобы политика использовалась,
требуется зарегистрировать политику
[CardTaskTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTaskTypeFilterPolicy.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[WhenTileGlobalFunc](M_Tessa_UI_Tiles_TileExtensions_WhenTileGlobalFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ITileGlobalExtension](T_Tessa_UI_Tiles_Extensions_ITileGlobalExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [TileExtensions](T_Tessa_UI_Tiles_TileExtensions.htm))  
[WhenTileLocalFunc](M_Tessa_UI_Tiles_TileExtensions_WhenTileLocalFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ITileLocalExtension](T_Tessa_UI_Tiles_Extensions_ITileLocalExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [TileExtensions](T_Tessa_UI_Tiles_TileExtensions.htm))  
[WhenTilePanel](M_Tessa_UI_Tiles_TileExtensions_WhenTilePanel.htm)|
Регистрирует политику фильтрации выполнения методов расширений по
местоположению боковой панели, которое входит в заданный список имён. Для
того, чтобы политика использовалась, требуется зарегистрировать политику
[TilePanelFilterPolicy](T_Tessa_UI_Tiles_Extensions_TilePanelFilterPolicy.htm).  
(Определяется [TileExtensions](T_Tessa_UI_Tiles_TileExtensions.htm))  
[WhenTilePanelFunc](M_Tessa_UI_Tiles_TileExtensions_WhenTilePanelFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ITilePanelExtension](T_Tessa_UI_Tiles_Extensions_ITilePanelExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
(Определяется [TileExtensions](T_Tessa_UI_Tiles_TileExtensions.htm))  
[WithCardModelTypeFilter](M_Tessa_UI_Cards_CardUIExtensions_WithCardModelTypeFilter.htm)|
Регистрирует политику фильтрации выполнения методов расширений UI по типам
карточек, указанных посредством политики
[ICardTypePolicy](T_Tessa_Cards_Extensions_ICardTypePolicy.htm).  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[WithDefaultConstructor](M_Tessa_Extensions_ExtensionExtensions_WithDefaultConstructor.htm)|
Регистрирует политику, указывающую на способ получения экземпляров расширений
посредством их конструкторов по умолчанию. Если класс расширения реализует
интерфейс [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm), то
для каждого созданного экземпляра будет вызвана асинхронная инициализация.  
(Определяется
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm))  
[WithFunc](M_Tessa_Extensions_ExtensionExtensions_WithFunc.htm)|  Регистрирует
политику, указывающую на способ получения экземпляров расширений посредством
заданной функции. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию непосредственно
внутри функции.  
(Определяется
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm))  
[WithInstance](M_Tessa_Extensions_ExtensionExtensions_WithInstance.htm)|
Регистрирует политику, указывающую на способ получения экземпляров расширений
посредством заданной ссылки на этот экземпляр. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию перед тем, как
передать экземпляр расширения в этот метод.  
(Определяется
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm))  
[WithLazy](M_Tessa_Extensions_ExtensionExtensions_WithLazy_3.htm)|
Регистрирует политику, указывающую на способ получения экземпляров расширений
посредством отложенной ссылки на экземпляр расширения. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию в лямбда-выражении,
переданном в другую реализацию метода.  
(Определяется
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm))  
[WithLazy](M_Tessa_Extensions_ExtensionExtensions_WithLazy_1.htm)|
Регистрирует политику, указывающую на способ отложенного получения экземпляров
расширений посредством заданной функции. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию в лямбда-выражении,
переданном в другую реализацию метода.  
(Определяется
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm))  
[WithLazy](M_Tessa_Extensions_ExtensionExtensions_WithLazy.htm)|  Регистрирует
политику, указывающую на способ отложенного получения экземпляров расширений
посредством заданной функции. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию внутри лямбда-
выражения.  
(Определяется
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm))  
[WithLazy](M_Tessa_Extensions_ExtensionExtensions_WithLazy_2.htm)|
Регистрирует политику, указывающую на способ получения экземпляров расширений
посредством отложенной ссылки на экземпляр расширения. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию в лямбда-выражении,
переданном в другую реализацию метода.  
(Определяется
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm))  
[WithOrder](M_Tessa_Extensions_ExtensionExtensions_WithOrder.htm)|
Регистрирует политику, указывающую порядок выполнения расширения в цепочке.  
(Определяется
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm))  
[WithPluginSchedulingFilter](M_Tessa_Platform_Plugins_PluginExtensions_WithPluginSchedulingFilter.htm)|
Регистрирует политику фильтрации выполнения методов расширений плагинов
[IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm), указанных
посредством политики
[IPluginSchedulingPolicy](T_Tessa_Platform_Plugins_IPluginSchedulingPolicy.htm).  
(Определяется
[PluginExtensions](T_Tessa_Platform_Plugins_PluginExtensions.htm))  
[WithScheduling](M_Tessa_Platform_Plugins_PluginExtensions_WithScheduling.htm)|
Регистрирует политику фильтрации выполнения методов расширений плагинов по
заданному способу диспетчеризации. Если способ диспетчеризации не задан, то
метод расширения не выполняется. Для того, чтобы политика использовалась,
требуется зарегистрировать политику
[PluginSchedulingFilterPolicy](T_Tessa_Platform_Plugins_PluginSchedulingFilterPolicy.htm).  
(Определяется
[PluginExtensions](T_Tessa_Platform_Plugins_PluginExtensions.htm))  
[WithSingleton](M_Tessa_Extensions_ExtensionExtensions_WithSingleton.htm)|
Регистрирует политику, указывающую на способ получения экземпляров расширений,
являющихся синглтонами, посредством их конструкторов по умолчанию. Если класс
расширения реализует интерфейс
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm), то для
созданного экземпляра один раз будет выполнена асинхронная инициализация.  
(Определяется
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm))  
[WithUnity](M_Tessa_Extensions_ExtensionExtensions_WithUnity.htm)|
Регистрирует политику, указывающую на способ получения экземпляров расширений
посредством заданного контейнера IUnityContainer. Если класс расширения
реализует интерфейс
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm), то
инициализация будет вызвана при каждом резолве из контейнера, т.е. для каждой
цепочки расширений.  
(Определяется
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
