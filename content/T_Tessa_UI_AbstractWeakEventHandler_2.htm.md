# AbstractWeakEventHandler<TSender, TEventArgs> \- класс
Позволяет навешивать обработку событий от централизованных источников событий
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class AbstractWeakEventHandler<TSender, TEventArgs> : IWeakEventHandler, 
    	IWeakEventListener
    where TEventArgs : EventArgs
VB __Копировать
     Public MustInherit Class AbstractWeakEventHandler(Of TSender, TEventArgs As EventArgs)
    	Implements IWeakEventHandler, IWeakEventListener
C++ __Копировать
    generic<typename TSender, typename TEventArgs>
    where TEventArgs : EventArgs
    public ref class AbstractWeakEventHandler abstract : IWeakEventHandler, 
    	IWeakEventListener
F# __Копировать
     [<AbstractClassAttribute>]
    type AbstractWeakEventHandler<'TSender, 'TEventArgs when 'TEventArgs : EventArgs> = 
        class
            interface IWeakEventHandler
            interface IWeakEventListener
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AbstractWeakEventHandler<TSender, TEventArgs>
Derived
[Tessa.UI.DelegatedWeakEventHandler<TSender,
TEventArgs>](T_Tessa_UI_DelegatedWeakEventHandler_2.htm)
Implements
    [IWeakEventListener](https://learn.microsoft.com/dotnet/api/system.windows.iweakeventlistener), [IWeakEventHandler](T_Tessa_UI_IWeakEventHandler.htm)
#### Параметры типа
TSender
    Тип отправителя
TEventArgs
    Тип параметров события
##  __Конструкторы
[AbstractWeakEventHandler<TSender,
TEventArgs>](M_Tessa_UI_AbstractWeakEventHandler_2__ctor.htm)| Инициализирует
новый экземпляр класса AbstractWeakEventHandler<TSender, TEventArgs>  
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
[Handle](M_Tessa_UI_AbstractWeakEventHandler_2_Handle.htm)|  Осуществляет
обработку события от централизованного обработчика  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SkipEvents](M_Tessa_UI_AbstractWeakEventHandler_2_SkipEvents.htm)|
Осуществляет запрет обработки событий поступающих от централизованного
обработчика событий.  
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
