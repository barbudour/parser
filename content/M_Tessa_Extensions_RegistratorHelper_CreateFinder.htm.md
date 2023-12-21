# RegistratorHelper.CreateFinder - метод
Создаёт объект, позволяющий осуществлять поиск типов
[IRegistrator](T_Tessa_Extensions_IRegistrator.htm) в указанном каталоге со
сборками.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IFinder<RegistratorImportingItem> CreateFinder(
    	IAssemblyCatalog catalog
    )
VB __Копировать
     Public Shared Function CreateFinder ( 
    	catalog As IAssemblyCatalog
    ) As IFinder(Of RegistratorImportingItem)
C++ __Копировать
     public:
    static IFinder<RegistratorImportingItem^>^ CreateFinder(
    	IAssemblyCatalog^ catalog
    )
F# __Копировать
     static member CreateFinder : 
            catalog : IAssemblyCatalog -> IFinder<RegistratorImportingItem> 
#### Параметры
catalog [IAssemblyCatalog](T_Tessa_Platform_Composition_IAssemblyCatalog.htm)
    Каталог со сборками, в котором будут найдены плагины.
#### Возвращаемое значение
[IFinder](T_Tessa_Platform_Composition_IFinder_1.htm)<[RegistratorImportingItem](T_Tessa_Extensions_RegistratorImportingItem.htm)>  
Объект, позволяющий осуществлять поиск типов.
##  __См. также
#### Ссылки
[RegistratorHelper - ](T_Tessa_Extensions_RegistratorHelper.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
