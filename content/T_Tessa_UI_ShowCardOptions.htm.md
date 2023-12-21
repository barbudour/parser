# ShowCardOptions - класс
Настройки отображения карточки.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class ShowCardOptions
VB __Копировать
     Public Class ShowCardOptions
C++ __Копировать
     public ref class ShowCardOptions
F# __Копировать
     type ShowCardOptions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ShowCardOptions
Derived
[Tessa.UI.CreateCardOptions](T_Tessa_UI_CreateCardOptions.htm)
[Tessa.UI.OpenCardOptions](T_Tessa_UI_OpenCardOptions.htm)
##  __Конструкторы
[ShowCardOptions](M_Tessa_UI_ShowCardOptions__ctor.htm)| Инициализирует новый
экземпляр класса ShowCardOptions  
---|---  
##  __Свойства
[AlwaysNewTab](P_Tessa_UI_ShowCardOptions_AlwaysNewTab.htm)|  Признак того,
что карточка всегда открывается в новой вкладке. Если значение равно false, то
вместо открытия карточки может быть выбрана вкладка, в которой уже открыта
карточка с этим идентификатором.  
---|---  
[DialogWindowModifierAction](P_Tessa_UI_ShowCardOptions_DialogWindowModifierAction.htm)|
Метод, который вызывается для объекта окна
[TessaWindow](T_Tessa_UI_Windows_TessaWindow.htm) перед тем, как карточка
будет отображена в диалоговом окне. Не учитывается при отображении во вкладке.
По умолчанию равно null, при этом не выполняется дополнительных действий.  
[DisplayValue](P_Tessa_UI_ShowCardOptions_DisplayValue.htm)|  Отображаемое имя
карточки, используемое при отсутствии Digest, или null, если отображаемое имя
вычисляется автоматически.  
[HideParentWindow](P_Tessa_UI_ShowCardOptions_HideParentWindow.htm)|  Признак
того, что при открытии окна диалога родительское окно должно быть скрыто. Не
скрывает основное окно приложения. Не учитывается при отображении во вкладке.  
[IgnorePreviouslyOpenedTab](P_Tessa_UI_ShowCardOptions_IgnorePreviouslyOpenedTab.htm)|
Признак того, что вкладка с уже открытой карточкой с тем же идентификатором
игнорируется и не активируется, т.е. всегда открывается новая вкладка.  
[OpenInFullscreen](P_Tessa_UI_ShowCardOptions_OpenInFullscreen.htm)|  Признак,
что диалог нужно открыть в полноэкранном режиме.  
[OpenToTheRightOfSelectedTab](P_Tessa_UI_ShowCardOptions_OpenToTheRightOfSelectedTab.htm)|
Если будет открыта новая вкладка (а не выбрана уже существующая), то она будет
открыта справа от текущей выбранной вкладки. В противном случае вкладка
добавляется в конец.  
[RestoreWindowLocationToParent](P_Tessa_UI_ShowCardOptions_RestoreWindowLocationToParent.htm)|
Признак того, что при закрытии окна диалога его позиция и размеры должны быть
использованы для вновь открытого родительского окна. Не изменяет размеры
основного окна приложения. Учитывается только при использовании флага
[HideParentWindow](P_Tessa_UI_ShowCardOptions_HideParentWindow.htm). Не
учитывается при отображении во вкладке.  
[ShowOnlyFirstTab](P_Tessa_UI_ShowCardOptions_ShowOnlyFirstTab.htm)|  Признак,
что нужно показывать только первую вкладку карточки без заголовка.  
[Splash](P_Tessa_UI_ShowCardOptions_Splash.htm)|  Внешний объект сплэш-окна
[Tessa.Platform.ISplash](Tessa.Platform.ISplash), при отображении которого
выполняется операция с карточкой, или null если сплэш-окно не отображается.
Объект окна должен быть в блоке using, внутри которого выполняемая операция с
карточкой. Сплэш-окно может быть скрыто внутри метода в случае, если операция
с карточкой производится с открытием диалогового окна.  
[UseParentWindowLocation](P_Tessa_UI_ShowCardOptions_UseParentWindowLocation.htm)|
Признак того, что при открытии окна диалога в качестве позиции и размеров
открываемого окна должны использоваться настройки родительского окна.
Учитывается только при использовании флага
[HideParentWindow](P_Tessa_UI_ShowCardOptions_HideParentWindow.htm). Не
учитывается при отображении во вкладке.  
[WithDialogWallpaper](P_Tessa_UI_ShowCardOptions_WithDialogWallpaper.htm)|
Признак того, что при отображении в диалоге должно отображаться фоновое
изображение. Не учитывается при отображении во вкладке. По умолчанию равно
true.  
[WithUIExtensions](P_Tessa_UI_ShowCardOptions_WithUIExtensions.htm)|  Признак
того, что должны выполняться UI расширения при действиях с карточкой. Не
учитывается при отображении объекта
[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm), переданного в метод
снаружи. По умолчанию равно true.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
