# AssemblyRegistratorFinder.Find - метод
Выполняет поиск объектов регистраторов и возвращает список объектов,
описывающих искомые объекты.
##  __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IList<RegistratorImportingItem> Find()
VB __Копировать
     Public Function Find As IList(Of RegistratorImportingItem)
C++ __Копировать
     public:
    virtual IList<RegistratorImportingItem^>^ Find() sealed
F# __Копировать
     abstract Find : unit -> IList<RegistratorImportingItem> 
    override Find : unit -> IList<RegistratorImportingItem> 
#### Возвращаемое значение
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[RegistratorImportingItem](T_Tessa_Extensions_RegistratorImportingItem.htm)>  
Список объектов, описывающих объекты регистраторов.
#### Реализации
[IFinder<T>.Find()](M_Tessa_Platform_Composition_IFinder_1_Find.htm)  
##  __См. также
#### Ссылки
[AssemblyRegistratorFinder -
](T_Tessa_Extensions_AssemblyRegistratorFinder.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
