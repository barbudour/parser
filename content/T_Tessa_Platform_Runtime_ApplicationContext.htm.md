# ApplicationContext - класс
Контекст, связанный с запуском или завершением приложения.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApplicationContext : IApplicationContext
VB __Копировать
     Public NotInheritable Class ApplicationContext
    	Implements IApplicationContext
C++ __Копировать
     public ref class ApplicationContext sealed : IApplicationContext
F# __Копировать
     [<SealedAttribute>]
    type ApplicationContext = 
        class
            interface IApplicationContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationContext
Implements
    [IApplicationContext](T_Tessa_Platform_Runtime_IApplicationContext.htm)
##  __Конструкторы
[ApplicationContext](M_Tessa_Platform_Runtime_ApplicationContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Application](P_Tessa_Platform_Runtime_ApplicationContext_Application.htm)|
Приложение, с которым связан контекст.  
---|---  
[ExecuteCommandFunc](P_Tessa_Platform_Runtime_ApplicationContext_ExecuteCommandFunc.htm)|
Функция, выполняющая нестандартную команду, полученную из командной строки,
или null, если функция не задана.  
[Info](P_Tessa_Platform_Runtime_ApplicationContext_Info.htm)| Дополнительная
информация, связанная с приложением.  
[LaunchParameters](P_Tessa_Platform_Runtime_ApplicationContext_LaunchParameters.htm)|
Параметры запуска приложения, которые были указаны при запуске.  
[LaunchResult](P_Tessa_Platform_Runtime_ApplicationContext_LaunchResult.htm)|
Результат запуска приложения или null, если приложение ещё не было запущено.  
[Parameters](P_Tessa_Platform_Runtime_ApplicationContext_Parameters.htm)|
Параметры запуска приложения, которые были определены в процессе запуска.  
[ParseCommandFunc](P_Tessa_Platform_Runtime_ApplicationContext_ParseCommandFunc.htm)|
Функция, выполняющая разбора нестандартного аргумента командной строки, или
null, если функция не задана.  
[ValidationResult](P_Tessa_Platform_Runtime_ApplicationContext_ValidationResult.htm)|
Сообщения валидации.  
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
[ResetValidationResult](M_Tessa_Platform_Runtime_ApplicationContext_ResetValidationResult.htm)|
Очищает результат валидации [Tessa.Platform.Runtime.IApplicationContext], т.о.
его можно будет заполнять новыми сообщениями.  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
