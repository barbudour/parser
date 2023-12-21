# IAssemblyResolver.TryResolve - метод
Получает сборку, в процессе чего может выполняться загрузка сборки. Возвращает
null, то считается, что сборка была загружена, но она должна игнорироваться,
например, если она уже была загружена и проверена ранее.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     Assembly TryResolve(
    	AssemblyLoadContext context
    )
VB __Копировать
     Function TryResolve ( 
    	context As AssemblyLoadContext
    ) As Assembly
C++ __Копировать
    Assembly^ TryResolve(
    	AssemblyLoadContext^ context
    )
F# __Копировать
     abstract TryResolve : 
            context : AssemblyLoadContext -> Assembly 
#### Параметры
context
[AssemblyLoadContext](https://learn.microsoft.com/dotnet/api/system.runtime.loader.assemblyloadcontext)
#### Возвращаемое значение
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)  
Полученная сборка или null, если сборка должна игнорироваться.
## __См. также
#### Ссылки
[IAssemblyResolver - ](T_Chronos_Platform_Composition_IAssemblyResolver.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
