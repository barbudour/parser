# CommonHelper.RemoveSuppressResolveFailWarningForAssembly - метод
Удаляет указанное имя из списка простых имён для сборок, для которых не
выводятся предупреждения в логе при невозможности их загрузить. Возвращает
признак того, что сборка присутствовала в списке до удаления.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool RemoveSuppressResolveFailWarningForAssembly(
    	string assemblyName
    )
VB __Копировать
     Public Shared Function RemoveSuppressResolveFailWarningForAssembly ( 
    	assemblyName As String
    ) As Boolean
C++ __Копировать
     public:
    static bool RemoveSuppressResolveFailWarningForAssembly(
    	String^ assemblyName
    )
F# __Копировать
     static member RemoveSuppressResolveFailWarningForAssembly : 
            assemblyName : string -> bool 
#### Параметры
assemblyName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Простое имя сборки. Обычно это имя файла без расширения. Не должно быть равно null или пустой строке. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если сборка с указанным именем присутствовала в списке до удаления;
false в противном случае.
## __См. также
#### Ссылки
[CommonHelper - ](T_Chronos_Platform_CommonHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
