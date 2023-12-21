# AssemblyResolver - конструктор
Создаёт экземпляр класса с указанием значений его свойств и методов.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public AssemblyResolver(
    	Func<AssemblyLoadContext, Assembly> tryResolveAssemblyFunc,
    	string filePath = null
    )
VB __Копировать
     Public Sub New ( 
    	tryResolveAssemblyFunc As Func(Of AssemblyLoadContext, Assembly),
    	Optional filePath As String = Nothing
    )
C++ __Копировать
     public:
    AssemblyResolver(
    	Func<AssemblyLoadContext^, Assembly^>^ tryResolveAssemblyFunc, 
    	String^ filePath = nullptr
    )
F# __Копировать
     new : 
            tryResolveAssemblyFunc : Func<AssemblyLoadContext, Assembly> * 
            ?filePath : string 
    (* Defaults:
            let _filePath = defaultArg filePath null
    *)
    -> AssemblyResolver
#### Параметры
tryResolveAssemblyFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[AssemblyLoadContext](https://learn.microsoft.com/dotnet/api/system.runtime.loader.assemblyloadcontext),
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)>
     Функция, получающая сборку. В ходе работы функции может выполняться загрузка сборки. Если функция возвращает null, то считается, что сборка была загружена, но она должна игнорироваться, например, если она уже была загружена и проверена ранее. Не должна быть равна null. 
filePath [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Путь к файлу со сборкой или null, если информация о местоположении сборки неизвестна или сборка не располагается в файле на диске. 
## __См. также
#### Ссылки
[AssemblyResolver - ](T_Chronos_Platform_Composition_AssemblyResolver.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
