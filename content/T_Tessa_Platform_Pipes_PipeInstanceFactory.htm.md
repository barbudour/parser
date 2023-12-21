# PipeInstanceFactory - класс
Фабрика экземпляров объектов, используемых в канале, время жизни которых
контролируется объектом
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeInstanceFactory : IPipeInstanceFactory
VB __Копировать
     Public Class PipeInstanceFactory
    	Implements IPipeInstanceFactory
C++ __Копировать
     public ref class PipeInstanceFactory : IPipeInstanceFactory
F# __Копировать
     type PipeInstanceFactory = 
        class
            interface IPipeInstanceFactory
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeInstanceFactory
Implements
    [IPipeInstanceFactory](T_Tessa_Platform_Pipes_IPipeInstanceFactory.htm)
##  __Заметки
Наследники класса могут переопределить методы и свойства класса.
## __Конструкторы
[PipeInstanceFactory](M_Tessa_Platform_Pipes_PipeInstanceFactory__ctor.htm)|
Инициализирует новый экземпляр класса PipeInstanceFactory  
---|---  
##  __Свойства
[CreateInstanceFuncByTypes](P_Tessa_Platform_Pipes_PipeInstanceFactory_CreateInstanceFuncByTypes.htm)|
Функции создания объектов, зарегистрированные по типу объекта.  
---|---  
## __Методы
[CreateInstanceAsync](M_Tessa_Platform_Pipes_PipeInstanceFactory_CreateInstanceAsync.htm)|
Создаёт экземпляр объекта, который ранее был зарегистрирован по заданному
типу. Возвращённый объект приводится к типу type и не равен null.  
---|---  
[CreateInstanceCoreAsync](M_Tessa_Platform_Pipes_PipeInstanceFactory_CreateInstanceCoreAsync.htm)|
Создаёт экземпляр объекта, который ранее был зарегистрирован по заданному
типу. Возвращённый объект приводится к типу type и не равен null.  
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
[Register](M_Tessa_Platform_Pipes_PipeInstanceFactory_Register.htm)|
Регистрирует функцию создания экземпляра объекта по заданному типу type.  
[RegisterCore](M_Tessa_Platform_Pipes_PipeInstanceFactory_RegisterCore.htm)|
Регистрирует функцию создания экземпляра объекта по заданному типу type.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[CreateInstanceAsync<T>](M_Tessa_Platform_Pipes_PipesExtensions_CreateInstanceAsync__1.htm)|
Создаёт экземпляр объекта, который ранее был зарегистрирован по заданному
типу. Возвращённый объект приводится к типу T и не равен null.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Register<T>](M_Tessa_Platform_Pipes_PipesExtensions_Register__1.htm)|
Регистрирует функцию создания экземпляра объекта по заданному типу T.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
