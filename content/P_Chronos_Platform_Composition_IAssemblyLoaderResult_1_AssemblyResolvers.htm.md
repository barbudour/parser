# IAssemblyLoaderResult<TMetadata>.AssemblyResolvers - свойство
Объекты, выполнявшие загрузку сборок в процессе экспорта метаинформации.
##  __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
    IReadOnlyList<IAssemblyResolver> AssemblyResolvers { get; }
VB __Копировать
     ReadOnly Property AssemblyResolvers As IReadOnlyList(Of IAssemblyResolver)
    	Get
C++ __Копировать
    property IReadOnlyList<IAssemblyResolver^>^ AssemblyResolvers {
    	IReadOnlyList<IAssemblyResolver^>^ get ();
    }
F# __Копировать
     abstract AssemblyResolvers : IReadOnlyList<IAssemblyResolver> with get
#### Значение свойства
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[IAssemblyResolver](T_Chronos_Platform_Composition_IAssemblyResolver.htm)>
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[IAssemblyLoaderResult<TMetadata> \-
](T_Chronos_Platform_Composition_IAssemblyLoaderResult_1.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
