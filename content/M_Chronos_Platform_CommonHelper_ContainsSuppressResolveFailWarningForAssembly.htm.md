# CommonHelper.ContainsSuppressResolveFailWarningForAssembly - метод
Возвращает признак того, что указанное имя входит в список простых имён для
сборок, для которых не выводятся предупреждения в логе при невозможности их
загрузить.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool ContainsSuppressResolveFailWarningForAssembly(
    	string assemblyName
    )
VB __Копировать
     Public Shared Function ContainsSuppressResolveFailWarningForAssembly ( 
    	assemblyName As String
    ) As Boolean
C++ __Копировать
     public:
    static bool ContainsSuppressResolveFailWarningForAssembly(
    	String^ assemblyName
    )
F# __Копировать
     static member ContainsSuppressResolveFailWarningForAssembly : 
            assemblyName : string -> bool 
#### Параметры
assemblyName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Простое имя сборки. Обычно это имя файла без расширения. Может быть равно null или пустой строке, в этом случае возвращается false. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если указанное имя входит в список простых имён для сборок, для которых
не выводятся предупреждения в логе при невозможности их загрузить; false в
противном случае.
## __См. также
#### Ссылки
[CommonHelper - ](T_Chronos_Platform_CommonHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
