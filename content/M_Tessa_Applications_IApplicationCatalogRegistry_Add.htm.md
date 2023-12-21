# IApplicationCatalogRegistry.Add - метод
Добавляет компонент catalog в контейнер. Добавляемый компонент должен быть не
равен null.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    IApplicationCatalog Add(
    	[NotNullAttribute] IApplicationCatalog catalog
    )
VB __Копировать
    <NotNullAttribute>
    Function Add ( 
    	<NotNullAttribute> catalog As IApplicationCatalog
    ) As IApplicationCatalog
C++ __Копировать
    [NotNullAttribute]
    IApplicationCatalog^ Add(
    	[NotNullAttribute] IApplicationCatalog^ catalog
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract Add : 
            [<NotNullAttribute>] catalog : IApplicationCatalog -> IApplicationCatalog 
#### Параметры
catalog [IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)
     Добавляемый в контейнер компонент. 
#### Возвращаемое значение
[IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)  
Возвращает добавленный в контейнер компонент
## __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Компонент catalog равен null  
---|---  
## __См. также
#### Ссылки
[IApplicationCatalogRegistry -
](T_Tessa_Applications_IApplicationCatalogRegistry.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
