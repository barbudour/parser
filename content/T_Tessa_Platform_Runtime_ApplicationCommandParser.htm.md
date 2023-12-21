# ApplicationCommandParser - класс
Объект, выполняющая разбор аргументов командной строки на команды
[IApplicationCommand](T_Tessa_Platform_Runtime_IApplicationCommand.htm).
Наследники класса могут переопределить разбор одного из аргументов командной
строки в методе [TryParseCommand(IApplicationContext, String,
String)](M_Tessa_Platform_Runtime_ApplicationCommandParser_TryParseCommand.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ApplicationCommandParser : IApplicationCommandParser
VB __Копировать
     Public Class ApplicationCommandParser
    	Implements IApplicationCommandParser
C++ __Копировать
     public ref class ApplicationCommandParser : IApplicationCommandParser
F# __Копировать
     type ApplicationCommandParser = 
        class
            interface IApplicationCommandParser
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationCommandParser
Implements
    [IApplicationCommandParser](T_Tessa_Platform_Runtime_IApplicationCommandParser.htm)
##  __Конструкторы
[ApplicationCommandParser](M_Tessa_Platform_Runtime_ApplicationCommandParser__ctor.htm)|
Инициализирует новый экземпляр класса ApplicationCommandParser  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Parse](M_Tessa_Platform_Runtime_ApplicationCommandParser_Parse.htm)|
Выполняет разбор заданных аргументов командной строки на параметры.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryParseCommand](M_Tessa_Platform_Runtime_ApplicationCommandParser_TryParseCommand.htm)|
Выполняет разбор заданного аргумента командной строки. Возвращает команду,
соответствующую аргументу, или null, если подходящая команда не найдена.  
[WithoutParams](M_Tessa_Platform_Runtime_ApplicationCommandParser_WithoutParams.htm)|
Выполняет разбор команды без параметров. Возвращает команду, если имя команды
в командной строке равно commandName, или null в противном случае.  
[WithParams](M_Tessa_Platform_Runtime_ApplicationCommandParser_WithParams.htm)|
Выполняет разбор команды с заданным именем и параметрами. Возвращает команду,
если имя команды в командной строке равно commandName, или null в противном
случае.  
## __Методы расширения
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
