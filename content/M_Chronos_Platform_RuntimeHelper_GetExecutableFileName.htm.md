# RuntimeHelper.GetExecutableFileName - метод
Возвращает имя основного исполняемого файла или полный путь к нему, если
параметр fullPath указан как true. При невозможности получить имя файла или
путь будет возвращено null или выброшено исключение.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetExecutableFileName(
    	bool fullPath = false,
    	bool keepDllPath = false,
    	Assembly assembly = null
    )
VB __Копировать
     Public Shared Function GetExecutableFileName ( 
    	Optional fullPath As Boolean = false,
    	Optional keepDllPath As Boolean = false,
    	Optional assembly As Assembly = Nothing
    ) As String
C++ __Копировать
     public:
    static String^ GetExecutableFileName(
    	bool fullPath = false, 
    	bool keepDllPath = false, 
    	Assembly^ assembly = nullptr
    )
F# __Копировать
     static member GetExecutableFileName : 
            ?fullPath : bool * 
            ?keepDllPath : bool * 
            ?assembly : Assembly 
    (* Defaults:
            let _fullPath = defaultArg fullPath false
            let _keepDllPath = defaultArg keepDllPath false
            let _assembly = defaultArg assembly null
    *)
    -> string 
#### Параметры
fullPath [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
     Признак того, что требуется вернуть полный путь к основному исполняемому файлу вместо имени. 
keepDllPath [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
     Признак того, что если путь определяеся как файл с расширением .dll, то надо оставить это расширение вместо того, чтобы заменять его на исполняемое в текущей ОС, т.е. .exe для Windows, без расширения для Linux. 
assembly
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)
(Optional)
    Сборка, для которой требуется получить путь к исполняемому файлу, или null, если выполняется поиск для текущего файла.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Имя основного исполняемого файла или полный путь к нему.
##  __См. также
#### Ссылки
[RuntimeHelper - ](T_Chronos_Platform_RuntimeHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
