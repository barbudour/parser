# IConsoleScriptMetadata - интерфейс
Метаинформация по атрибуту
[ConsoleScriptAttribute](T_Tessa_Platform_ConsoleApps_ConsoleScriptAttribute.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IConsoleScriptMetadata : ISerializableMetadata<IConsoleScriptMetadata>
VB __Копировать
     Public Interface IConsoleScriptMetadata
    	Inherits ISerializableMetadata(Of IConsoleScriptMetadata)
C++ __Копировать
     public interface class IConsoleScriptMetadata : ISerializableMetadata<IConsoleScriptMetadata^>
F# __Копировать
     type IConsoleScriptMetadata = 
        interface
            interface ISerializableMetadata<IConsoleScriptMetadata>
        end
Implements
    [ISerializableMetadata](T_Tessa_Platform_Composition_ISerializableMetadata_1.htm)<IConsoleScriptMetadata>
##  __Свойства
[Name](P_Tessa_Platform_ConsoleApps_IConsoleScriptMetadata_Name.htm)|  Имя
скрипта, которое указывается в параметрах консольной команды для запуска
скрипта. Должно быть уникальным среди всех сборок расширений, подключённых к
консольной утилите. По умолчанию (если указаны null или пустая строка)
соотносится с полным именем типа для класса, к которому применён атрибут
[ConsoleScriptAttribute](T_Tessa_Platform_ConsoleApps_ConsoleScriptAttribute.htm).  
---|---  
## __Методы
[GetSerializable](M_Tessa_Platform_Composition_ISerializableMetadata_1_GetSerializable.htm)|
Возвращает метаинформацию, которая может быть сериализована через атрибут
[System.SerializableAttribute]. Если текущий объект уже сериализуется, то он
может вернуть себя же.  
(Унаследован от
[ISerializableMetadata<TMetadata>](T_Tessa_Platform_Composition_ISerializableMetadata_1.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.ConsoleApps - пространство
имён](N_Tessa_Platform_ConsoleApps.htm)
