# MetadataExportItem<TMetadata>.ResolveAssemblyFunc - свойство
Функция, выполняющая загрузку сборки, в которой размещается тип, или null,
если загруженная сборка недоступна.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Func<AssemblyLoadContext, Assembly> ResolveAssemblyFunc { get; }
VB __Копировать
     Public ReadOnly Property ResolveAssemblyFunc As Func(Of AssemblyLoadContext, Assembly)
    	Get
C++ __Копировать
     public:
    virtual property Func<AssemblyLoadContext^, Assembly^>^ ResolveAssemblyFunc {
    	Func<AssemblyLoadContext^, Assembly^>^ get () sealed;
    }
F# __Копировать
     abstract ResolveAssemblyFunc : Func<AssemblyLoadContext, Assembly> with get
    override ResolveAssemblyFunc : Func<AssemblyLoadContext, Assembly> with get
#### Значение свойства
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[AssemblyLoadContext](https://learn.microsoft.com/dotnet/api/system.runtime.loader.assemblyloadcontext),
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)>
#### Реализации
[IMetadataExportItem<TMetadata>.ResolveAssemblyFunc](P_Chronos_Platform_Composition_IMetadataExportItem_1_ResolveAssemblyFunc.htm)  
##  __См. также
#### Ссылки
[MetadataExportItem<TMetadata> \-
](T_Chronos_Platform_Composition_MetadataExportItem_1.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
