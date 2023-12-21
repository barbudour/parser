# UIContextActionOverridings - класс
Набор делегатов для переопределения действий в интерфейсе, связанных с UI
контекстом
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class UIContextActionOverridings : IUIContextActionOverridings
VB __Копировать
     Public Class UIContextActionOverridings
    	Implements IUIContextActionOverridings
C++ __Копировать
     public ref class UIContextActionOverridings : IUIContextActionOverridings
F# __Копировать
     type UIContextActionOverridings = 
        class
            interface IUIContextActionOverridings
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UIContextActionOverridings
Implements
    [IUIContextActionOverridings](T_Tessa_UI_IUIContextActionOverridings.htm)
##  __Конструкторы
[UIContextActionOverridings](M_Tessa_UI_UIContextActionOverridings__ctor.htm)|
Инициализирует новый экземпляр класса UIContextActionOverridings  
---|---  
##  __Свойства
[CreateCardAsync](P_Tessa_UI_UIContextActionOverridings_CreateCardAsync.htm)|
Переопределение действия на создание новой карточки
[CreateCardAsync(Nullable<Guid>, String, CreateCardOptions,
CancellationToken)](M_Tessa_UI_IUIHost_CreateCardAsync.htm)  
---|---  
[OpenCardAsync](P_Tessa_UI_UIContextActionOverridings_OpenCardAsync.htm)|
Переопределение действия на открытие карточки [OpenCardAsync(Nullable<Guid>,
Nullable<Guid>, String, OpenCardOptions,
CancellationToken)](M_Tessa_UI_IUIHost_OpenCardAsync.htm)  
[ShowCardEditorAsync](P_Tessa_UI_UIContextActionOverridings_ShowCardEditorAsync.htm)|
Переопределение действия на открытие карточки по CardEditor
IUIHost.ShowCardAsync  
[ShowCardModelAsync](P_Tessa_UI_UIContextActionOverridings_ShowCardModelAsync.htm)|
Переопределение действия на открытие карточки по модели IUIHost.ShowCardAsync  
##  __Методы
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
