# AssemblyResolver.TryResolve - метод
Получает сборку, в процессе чего может выполняться загрузка сборки. Возвращает
null, то считается, что сборка была загружена, но она должна игнорироваться,
например, если она уже была загружена и проверена ранее.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Assembly TryResolve(
    	AssemblyLoadContext context
    )
VB __Копировать
     Public Function TryResolve ( 
    	context As AssemblyLoadContext
    ) As Assembly
C++ __Копировать
     public:
    virtual Assembly^ TryResolve(
    	AssemblyLoadContext^ context
    ) sealed
F# __Копировать
     abstract TryResolve : 
            context : AssemblyLoadContext -> Assembly 
    override TryResolve : 
            context : AssemblyLoadContext -> Assembly 
#### Параметры
context
[AssemblyLoadContext](https://learn.microsoft.com/dotnet/api/system.runtime.loader.assemblyloadcontext)
#### Возвращаемое значение
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)  
Полученная сборка или null, если сборка должна игнорироваться.
#### Реализации
[IAssemblyResolver.TryResolve(AssemblyLoadContext)](M_Chronos_Platform_Composition_IAssemblyResolver_TryResolve.htm)  
##  __См. также
#### Ссылки
[AssemblyResolver - ](T_Chronos_Platform_Composition_AssemblyResolver.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
