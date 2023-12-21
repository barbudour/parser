# IMetadataExportItem<TMetadata>.ResolveAssemblyFunc - свойство
Функция, выполняющая загрузку сборки, в которой размещается тип, или null,
если загруженная сборка недоступна.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
    Func<AssemblyLoadContext, Assembly> ResolveAssemblyFunc { get; }
VB __Копировать
     ReadOnly Property ResolveAssemblyFunc As Func(Of AssemblyLoadContext, Assembly)
    	Get
C++ __Копировать
    property Func<AssemblyLoadContext^, Assembly^>^ ResolveAssemblyFunc {
    	Func<AssemblyLoadContext^, Assembly^>^ get ();
    }
F# __Копировать
     abstract ResolveAssemblyFunc : Func<AssemblyLoadContext, Assembly> with get
#### Значение свойства
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[AssemblyLoadContext](https://learn.microsoft.com/dotnet/api/system.runtime.loader.assemblyloadcontext),
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)>
##  __См. также
#### Ссылки
[IMetadataExportItem<TMetadata> \-
](T_Chronos_Platform_Composition_IMetadataExportItem_1.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
