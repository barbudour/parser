# CommonHelper.AddSuppressResolveFailWarningForAssembly - метод
Добавляет указанное имя в список простых имён для сборок, для которых не
выводятся предупреждения в логе при невозможности их загрузить. Добавьте сюда
сборки, например "System.Data.SqlClient", если возможное отсутствие такой
сборки является корректным для используемых библиотек.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static void AddSuppressResolveFailWarningForAssembly(
    	string assemblyName
    )
VB __Копировать
     Public Shared Sub AddSuppressResolveFailWarningForAssembly ( 
    	assemblyName As String
    )
C++ __Копировать
     public:
    static void AddSuppressResolveFailWarningForAssembly(
    	String^ assemblyName
    )
F# __Копировать
     static member AddSuppressResolveFailWarningForAssembly : 
            assemblyName : string -> unit 
#### Параметры
assemblyName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Простое имя сборки. Обычно это имя файла без расширения. Не должно быть равно null или пустой строке. 
## __См. также
#### Ссылки
[CommonHelper - ](T_Chronos_Platform_CommonHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
