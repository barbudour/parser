# Command - класс
Represents a command that performs an action.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class Command
VB __Копировать
     Public MustInherit Class Command
C++ __Копировать
     public ref class Command abstract
F# __Копировать
     [<AbstractClassAttribute>]
    type Command = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ Command
Derived
[Tessa.Platform.CommandLine.CommandContext](T_Tessa_Platform_CommandLine_CommandContext.htm)
[Tessa.Platform.CommandLine.DelegateCommand](T_Tessa_Platform_CommandLine_DelegateCommand.htm)
##  __Конструкторы
[Command(String)](M_Tessa_Platform_CommandLine_Command__ctor.htm)|
Initializes a new instance of the Command class using the specified command
name.  
---|---  
[Command(String, String)](M_Tessa_Platform_CommandLine_Command__ctor_1.htm)|
Initializes a new instance of the Command class using the specified command
name and description.  
## __Свойства
[Description](P_Tessa_Platform_CommandLine_Command_Description.htm)|  Gets the
description of the command.  
---|---  
[Name](P_Tessa_Platform_CommandLine_Command_Name.htm)|  Gets the name of the
command.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[ExecuteAsync()](M_Tessa_Platform_CommandLine_Command_ExecuteAsync.htm)|
Executes a command using standard IO streams and arguments which will be read
from the input stream.  
[ExecuteAsync(ArgumentEnumerator)](M_Tessa_Platform_CommandLine_Command_ExecuteAsync_11.htm)|
Executes a command using standard IO streams and specified arguments.  
[ExecuteAsync(String)](M_Tessa_Platform_CommandLine_Command_ExecuteAsync_9.htm)|
Executes a command using standard IO streams and specified arguments.  
[ExecuteAsync(String[])](M_Tessa_Platform_CommandLine_Command_ExecuteAsync_10.htm)|
Executes a command using standard IO streams and specified arguments.  
[ExecuteAsync(TextReader,
TextWriter)](M_Tessa_Platform_CommandLine_Command_ExecuteAsync_1.htm)|
Executes a command using specified IO streams and arguments which will be read
from the input stream.  
[ExecuteAsync(TextReader, TextWriter,
TextWriter)](M_Tessa_Platform_CommandLine_Command_ExecuteAsync_2.htm)|
Executes a command using specified IO streams and arguments which will be read
from the input stream.  
[ExecuteAsync(TextReader, TextWriter,
String)](M_Tessa_Platform_CommandLine_Command_ExecuteAsync_6.htm)|  Executes a
command using specified IO streams and arguments.  
[ExecuteAsync(TextReader, TextWriter,
String[])](M_Tessa_Platform_CommandLine_Command_ExecuteAsync_7.htm)|  Executes
a command using specified IO streams and arguments.  
[ExecuteAsync(TextReader, TextWriter,
ArgumentEnumerator)](M_Tessa_Platform_CommandLine_Command_ExecuteAsync_8.htm)|
Executes a command using specified IO streams and arguments.  
[ExecuteAsync(TextReader, TextWriter, TextWriter,
String)](M_Tessa_Platform_CommandLine_Command_ExecuteAsync_3.htm)|  Executes a
command using specified IO streams and arguments.  
[ExecuteAsync(TextReader, TextWriter, TextWriter,
String[])](M_Tessa_Platform_CommandLine_Command_ExecuteAsync_4.htm)|  Executes
a command using specified IO streams and arguments.  
[ExecuteAsync(TextReader, TextWriter, TextWriter,
ArgumentEnumerator)](M_Tessa_Platform_CommandLine_Command_ExecuteAsync_5.htm)|
Executes a command using specified IO streams and arguments.  
[ExecuteCoreAsync](M_Tessa_Platform_CommandLine_Command_ExecuteCoreAsync.htm)|
When overridden in a derived class, provides execution logic.  
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
##  __Операторы
[ Implicit(Delegate to
Command)](M_Tessa_Platform_CommandLine_Command_op_Implicit.htm)|  
---|---  
## __Методы расширения
[ExecuteAllAsync](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteAllAsync.htm)|
Continuously executes a command using standard IO streams until the input
stream returns null or a CommandCanceledException was thrown.  
(Определяется
[CommandExtensions](T_Tessa_Platform_CommandLine_CommandExtensions.htm))  
---|---  
[ExecuteAllAsync](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteAllAsync_1.htm)|  
(Определяется
[CommandExtensions](T_Tessa_Platform_CommandLine_CommandExtensions.htm))  
[ExecuteAllAsync](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteAllAsync_2.htm)|
Continuously executes a command using specified IO streams until the input
stream returns null or a CommandCanceledException was thrown.  
(Определяется
[CommandExtensions](T_Tessa_Platform_CommandLine_CommandExtensions.htm))  
[ExecuteAllAsync](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteAllAsync_3.htm)|
Continuously executes a command using specified IO streams until the input
stream returns null or a CommandCanceledException was thrown.  
(Определяется
[CommandExtensions](T_Tessa_Platform_CommandLine_CommandExtensions.htm))  
[ExecuteAllAsync](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteAllAsync_4.htm)|  
(Определяется
[CommandExtensions](T_Tessa_Platform_CommandLine_CommandExtensions.htm))  
[ExecuteSingleAsync](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteSingleAsync.htm)|
Executes a command using standard IO streams.  
(Определяется
[CommandExtensions](T_Tessa_Platform_CommandLine_CommandExtensions.htm))  
[ExecuteSingleAsync](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteSingleAsync_1.htm)|  
(Определяется
[CommandExtensions](T_Tessa_Platform_CommandLine_CommandExtensions.htm))  
[ExecuteSingleAsync](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteSingleAsync_2.htm)|
Executes a command using specified IO streams.  
(Определяется
[CommandExtensions](T_Tessa_Platform_CommandLine_CommandExtensions.htm))  
[ExecuteSingleAsync](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteSingleAsync_3.htm)|
Executes a command using specified IO streams.  
(Определяется
[CommandExtensions](T_Tessa_Platform_CommandLine_CommandExtensions.htm))  
[ExecuteSingleAsync](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteSingleAsync_4.htm)|  
(Определяется
[CommandExtensions](T_Tessa_Platform_CommandLine_CommandExtensions.htm))  
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
