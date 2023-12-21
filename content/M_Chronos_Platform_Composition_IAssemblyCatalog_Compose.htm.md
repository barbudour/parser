# IAssemblyCatalog.Compose - метод
Составляет список объектов, выполняющих получение сборок для загрузки
экспортируемой метаинформации.
##  __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     void Compose(
    	IList<IAssemblyResolver> resolverList
    )
VB __Копировать
     Sub Compose ( 
    	resolverList As IList(Of IAssemblyResolver)
    )
C++ __Копировать
     void Compose(
    	IList<IAssemblyResolver^>^ resolverList
    )
F# __Копировать
     abstract Compose : 
            resolverList : IList<IAssemblyResolver> -> unit 
#### Параметры
resolverList
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IAssemblyResolver](T_Chronos_Platform_Composition_IAssemblyResolver.htm)>
    Список объектов, выполняющих получение сборок для загрузки экспортируемой метаинформации.
##  __См. также
#### Ссылки
[IAssemblyCatalog - ](T_Chronos_Platform_Composition_IAssemblyCatalog.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
