# RuntimeHelper.AssemblyResolveActualLocationFunc - свойство
Делегат, обеспечивающий алгоритм определения путей к файлу заданной сборки
вызовом
[GetActualLocationFolder(Assembly)](M_Chronos_Platform_PlatformExtensions_GetActualLocationFolder.htm).
Если делегат равен null (по умолчанию) или он возвращает null, то используется
стандартный алгоритм из метода
[GetLocationFileNameFromCodeBase(Assembly)](M_Chronos_Platform_PlatformExtensions_GetLocationFileNameFromCodeBase.htm),
определяющий местоположение сборки до того, как она могла быть скопирована
механизмом shadow copy.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static Func<Assembly, string> AssemblyResolveActualLocationFunc { get; set; }
VB __Копировать
     Public Shared Property AssemblyResolveActualLocationFunc As Func(Of Assembly, String)
    	Get
    	Set
C++ __Копировать
     public:
    static property Func<Assembly^, String^>^ AssemblyResolveActualLocationFunc {
    	Func<Assembly^, String^>^ get ();
    	void set (Func<Assembly^, String^>^ value);
    }
F# __Копировать
     static member AssemblyResolveActualLocationFunc : Func<Assembly, string> with get, set
#### Значение свойства
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly),
[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __См. также
#### Ссылки
[RuntimeHelper - ](T_Chronos_Platform_RuntimeHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
