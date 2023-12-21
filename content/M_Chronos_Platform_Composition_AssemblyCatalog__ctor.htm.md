# AssemblyCatalog(Func<AssemblyLoadContext, Assembly>) - конструктор
Создаёт экземпляр класса с указанием функции для получения сборки..
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public AssemblyCatalog(
    	Func<AssemblyLoadContext, Assembly> tryResolveAssemblyFunc
    )
VB __Копировать
     Public Sub New ( 
    	tryResolveAssemblyFunc As Func(Of AssemblyLoadContext, Assembly)
    )
C++ __Копировать
     public:
    AssemblyCatalog(
    	Func<AssemblyLoadContext^, Assembly^>^ tryResolveAssemblyFunc
    )
F# __Копировать
     new : 
            tryResolveAssemblyFunc : Func<AssemblyLoadContext, Assembly> -> AssemblyCatalog
#### Параметры
tryResolveAssemblyFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[AssemblyLoadContext](https://learn.microsoft.com/dotnet/api/system.runtime.loader.assemblyloadcontext),
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)>
     Функция, получающая сборку. В ходе работы функции может выполняться загрузка сборки. Не должна быть равна null, также не должна возвращать null. 
## __См. также
#### Ссылки
[AssemblyCatalog - ](T_Chronos_Platform_Composition_AssemblyCatalog.htm)
[AssemblyCatalog -
перегрузка](Overload_Chronos_Platform_Composition_AssemblyCatalog__ctor.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
