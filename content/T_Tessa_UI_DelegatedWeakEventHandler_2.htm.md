# DelegatedWeakEventHandler<TSender, TEventArgs> \- класс
Класс позволяющий делегировать обработку событий от централизованного
обработчика событий функции передаваемой в конструкторе
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class DelegatedWeakEventHandler<TSender, TEventArgs> : AbstractWeakEventHandler<TSender, TEventArgs>
    where TEventArgs : EventArgs
VB __Копировать
     Public Class DelegatedWeakEventHandler(Of TSender, TEventArgs As EventArgs)
    	Inherits AbstractWeakEventHandler(Of TSender, TEventArgs)
C++ __Копировать
    generic<typename TSender, typename TEventArgs>
    where TEventArgs : EventArgs
    public ref class DelegatedWeakEventHandler : public AbstractWeakEventHandler<TSender, TEventArgs>
F# __Копировать
     type DelegatedWeakEventHandler<'TSender, 'TEventArgs when 'TEventArgs : EventArgs> = 
        class
            inherit AbstractWeakEventHandler<'TSender, 'TEventArgs>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[AbstractWeakEventHandler](T_Tessa_UI_AbstractWeakEventHandler_2.htm)<TSender, TEventArgs> __ DelegatedWeakEventHandler<TSender, TEventArgs>
#### Параметры типа
TSender
    Тип источника события
TEventArgs
    Тип параметров события
##  __Конструкторы
[DelegatedWeakEventHandler<TSender,
TEventArgs>](M_Tessa_UI_DelegatedWeakEventHandler_2__ctor.htm)| Инициализирует
новый экземпляр класса DelegatedWeakEventHandler<TSender, TEventArgs>  
---|---  
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
[Handle](M_Tessa_UI_DelegatedWeakEventHandler_2_Handle.htm)|  Осуществляет
обработку события от централизованного обработчика  
(Переопределяет [AbstractWeakEventHandler<TSender, TEventArgs>.Handle(Type,
TSender, TEventArgs)](M_Tessa_UI_AbstractWeakEventHandler_2_Handle.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SkipEvents](M_Tessa_UI_AbstractWeakEventHandler_2_SkipEvents.htm)|
Осуществляет запрет обработки событий поступающих от централизованного
обработчика событий.  
(Унаследован от [AbstractWeakEventHandler<TSender,
TEventArgs>](T_Tessa_UI_AbstractWeakEventHandler_2.htm))  
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
