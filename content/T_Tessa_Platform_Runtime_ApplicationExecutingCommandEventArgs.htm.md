# ApplicationExecutingCommandEventArgs - класс
Аргументы события, связанные с выполнением команды, полученной из командной
строки.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApplicationExecutingCommandEventArgs : EventArgs
VB __Копировать
     Public NotInheritable Class ApplicationExecutingCommandEventArgs
    	Inherits EventArgs
C++ __Копировать
     public ref class ApplicationExecutingCommandEventArgs sealed : public EventArgs
F# __Копировать
     [<SealedAttribute>]
    type ApplicationExecutingCommandEventArgs = 
        class
            inherit EventArgs
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[EventArgs](https://learn.microsoft.com/dotnet/api/system.eventargs) __ ApplicationExecutingCommandEventArgs
##  __Конструкторы
[ApplicationExecutingCommandEventArgs](M_Tessa_Platform_Runtime_ApplicationExecutingCommandEventArgs__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Command](P_Tessa_Platform_Runtime_ApplicationExecutingCommandEventArgs_Command.htm)|
Команда, которую требуется выполнить.  
---|---  
[Context](P_Tessa_Platform_Runtime_ApplicationExecutingCommandEventArgs_Context.htm)|
Контекст, связанный с запуском или завершением приложения.  
[Handled](P_Tessa_Platform_Runtime_ApplicationExecutingCommandEventArgs_Handled.htm)|
Признак того, что команда была обработана. По умолчанию false. Если команда не
обработана ни одним обработчиком события, то для неё отображается
предупреждение.  
[Name](P_Tessa_Platform_Runtime_ApplicationExecutingCommandEventArgs_Name.htm)|
Имя команды в командной строке.  
[Parameter](P_Tessa_Platform_Runtime_ApplicationExecutingCommandEventArgs_Parameter.htm)|
Параметр команды в командной строке.  
## __Методы
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
[IsPropertyChanged](M_Tessa_UI_Controls_PropertyChangedHelper_IsPropertyChanged.htm)|
Проверяет наступление события изменения свойства propertyName  
(Определяется
[PropertyChangedHelper](T_Tessa_UI_Controls_PropertyChangedHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
