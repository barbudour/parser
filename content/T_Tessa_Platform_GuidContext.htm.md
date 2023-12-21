# GuidContext - класс
Контекст операции, связанной с заменой уникальных идентификаторов.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class GuidContext : IGuidContext
VB __Копировать
     Public NotInheritable Class GuidContext
    	Implements IGuidContext
C++ __Копировать
     public ref class GuidContext sealed : IGuidContext
F# __Копировать
     [<SealedAttribute>]
    type GuidContext = 
        class
            interface IGuidContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ GuidContext
Implements
    [IGuidContext](T_Tessa_Platform_IGuidContext.htm)
##  __Конструкторы
[GuidContext](M_Tessa_Platform_GuidContext__ctor.htm)|  Создаёт экземпляр
класса с указанием значений его свойств.  
---|---  
## __Свойства
[Current](P_Tessa_Platform_GuidContext_Current.htm)|  Текущий контекст
[IGuidContext](T_Tessa_Platform_IGuidContext.htm).  
---|---  
[HasCurrent](P_Tessa_Platform_GuidContext_HasCurrent.htm)|  Признак того, что
текущий код выполняется внутри операции с контекстом
[IGuidContext](T_Tessa_Platform_IGuidContext.htm), а свойство
[Current](P_Tessa_Platform_GuidContext_Current.htm) ссылается на
действительный контекст.  
[Replacer](P_Tessa_Platform_GuidContext_Replacer.htm)| Объект, выполняющий
замещение идентификаторов на сгенерированные идентификаторы.  
[Unknown](P_Tessa_Platform_GuidContext_Unknown.htm)|  Неизвестный контекст
[IGuidContext](T_Tessa_Platform_IGuidContext.htm).  
## __Методы
[Create](M_Tessa_Platform_GuidContext_Create.htm)|  Создаёт область операции,
в которой заданный контекст будет являться текущим.  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
