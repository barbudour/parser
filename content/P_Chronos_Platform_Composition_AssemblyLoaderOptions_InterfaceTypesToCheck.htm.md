# AssemblyLoaderOptions.InterfaceTypesToCheck - свойство
Типы интерфейсов, для которых надо проверить, что экспортируемый тип с
атрибутом их реализует.
##  __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public IList<Type> InterfaceTypesToCheck { get; }
VB __Копировать
     Public ReadOnly Property InterfaceTypesToCheck As IList(Of Type)
    	Get
C++ __Копировать
     public:
    virtual property IList<Type^>^ InterfaceTypesToCheck {
    	IList<Type^>^ get () sealed;
    }
F# __Копировать
     abstract InterfaceTypesToCheck : IList<Type> with get
    override InterfaceTypesToCheck : IList<Type> with get
#### Значение свойства
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[Type](https://learn.microsoft.com/dotnet/api/system.type)>
#### Реализации
[IAssemblyLoaderOptions.InterfaceTypesToCheck](P_Chronos_Platform_Composition_IAssemblyLoaderOptions_InterfaceTypesToCheck.htm)  
##  __См. также
#### Ссылки
[AssemblyLoaderOptions -
](T_Chronos_Platform_Composition_AssemblyLoaderOptions.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
