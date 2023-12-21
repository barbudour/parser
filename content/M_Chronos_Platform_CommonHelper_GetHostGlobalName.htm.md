# CommonHelper.GetHostGlobalName(Assembly, String) - метод
Возвращает глобально уникальное имя в пределах хоста для заданной сборки,
полученное по заданному локальному имени.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetHostGlobalName(
    	Assembly assembly,
    	string localName
    )
VB __Копировать
     Public Shared Function GetHostGlobalName ( 
    	assembly As Assembly,
    	localName As String
    ) As String
C++ __Копировать
     public:
    static String^ GetHostGlobalName(
    	Assembly^ assembly, 
    	String^ localName
    )
F# __Копировать
     static member GetHostGlobalName : 
            assembly : Assembly * 
            localName : string -> string 
#### Параметры
assembly
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)
    Сборка, для которой будет получено глобально уникальное имя.
localName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Локальное имя в пределах сборки assembly.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Глобально уникальное имя в пределах хоста для заданной сборки, полученное по
заданному локальному имени.
## __Заметки
Глобально уникальное имя в пределах хоста включает в себя отображаемое имя
заданной сборки и заданное локальное имя.
## __См. также
#### Ссылки
[CommonHelper - ](T_Chronos_Platform_CommonHelper.htm)
[GetHostGlobalName -
перегрузка](Overload_Chronos_Platform_CommonHelper_GetHostGlobalName.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
