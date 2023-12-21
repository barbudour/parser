# PipeInstanceContext - класс
Контекст, управляющий временем жизни экземпляров объектов, используемых в
канале.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PipeInstanceContext : IPipeInstanceContext
VB __Копировать
     Public NotInheritable Class PipeInstanceContext
    	Implements IPipeInstanceContext
C++ __Копировать
     public ref class PipeInstanceContext sealed : IPipeInstanceContext
F# __Копировать
     [<SealedAttribute>]
    type PipeInstanceContext = 
        class
            interface IPipeInstanceContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeInstanceContext
Implements
    [IPipeInstanceContext](T_Tessa_Platform_Pipes_IPipeInstanceContext.htm)
##  __Конструкторы
[PipeInstanceContext](M_Tessa_Platform_Pipes_PipeInstanceContext__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[Current](P_Tessa_Platform_Pipes_PipeInstanceContext_Current.htm)|  Текущий
контекст
[IPipeInstanceContext](T_Tessa_Platform_Pipes_IPipeInstanceContext.htm).  
---|---  
[HasCurrent](P_Tessa_Platform_Pipes_PipeInstanceContext_HasCurrent.htm)|
Признак того, что текущий код выполняется внутри операции с контекстом
[IPipeInstanceContext](T_Tessa_Platform_Pipes_IPipeInstanceContext.htm), а
свойство [Current](P_Tessa_Platform_Pipes_PipeInstanceContext_Current.htm)
ссылается на действительный контекст.  
[InstanceResolver](P_Tessa_Platform_Pipes_PipeInstanceContext_InstanceResolver.htm)|
Объект, управляющий временем жизни экземпляров объектов, используемых в
канале.  
[Unknown](P_Tessa_Platform_Pipes_PipeInstanceContext_Unknown.htm)|
Неизвестный контекст
[IPipeInstanceContext](T_Tessa_Platform_Pipes_IPipeInstanceContext.htm).  
## __Методы
[Create](M_Tessa_Platform_Pipes_PipeInstanceContext_Create.htm)|  Создаёт
область операции, в которой заданный контекст будет являться текущим.  
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
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
