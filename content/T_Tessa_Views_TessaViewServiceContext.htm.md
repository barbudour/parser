# TessaViewServiceContext - класс
Контекст для изменения текущего
[ITessaViewService](T_Tessa_Views_ITessaViewService.htm).
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class TessaViewServiceContext : ITessaViewServiceContext
VB __Копировать
     Public NotInheritable Class TessaViewServiceContext
    	Implements ITessaViewServiceContext
C++ __Копировать
     public ref class TessaViewServiceContext sealed : ITessaViewServiceContext
F# __Копировать
     [<SealedAttribute>]
    type TessaViewServiceContext = 
        class
            interface ITessaViewServiceContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaViewServiceContext
Implements
    [ITessaViewServiceContext](T_Tessa_Views_ITessaViewServiceContext.htm)
##  __Заметки
Используйте совместно с
[TessaViewServiceProxy](T_Tessa_Views_TessaViewServiceProxy.htm).
## __Конструкторы
[TessaViewServiceContext](M_Tessa_Views_TessaViewServiceContext__ctor.htm)|
Создаёт экземпляр класса с указанием сервиса, который должен быть изменён.  
---|---  
## __Свойства
[Current](P_Tessa_Views_TessaViewServiceContext_Current.htm)|  Текущий
контекст
[ITessaViewServiceContext](T_Tessa_Views_ITessaViewServiceContext.htm).  
---|---  
[HasCurrent](P_Tessa_Views_TessaViewServiceContext_HasCurrent.htm)|  Признак
того, что текущий код выполняется внутри операции с контекстом
[ITessaViewServiceContext](T_Tessa_Views_ITessaViewServiceContext.htm), а
свойство [Current](P_Tessa_Views_TessaViewServiceContext_Current.htm)
ссылается на действительный контекст.  
[Unknown](P_Tessa_Views_TessaViewServiceContext_Unknown.htm)|  Неизвестный
контекст
[ITessaViewServiceContext](T_Tessa_Views_ITessaViewServiceContext.htm).  
## __Методы
[Create](M_Tessa_Views_TessaViewServiceContext_Create.htm)|  Создаёт область
операции, в которой заданный контекст будет являться текущим.  
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
[GetService](M_Tessa_Views_TessaViewServiceContext_GetService.htm)|
Возвращает изменённый сервис
[ITessaViewService](T_Tessa_Views_ITessaViewService.htm) или null, если сервис
не изменён и должен использоваться стандартный сервис.  
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
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
