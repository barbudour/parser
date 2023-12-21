# ApplicationModelFactoryDelegate - делегат
Фабрика создания модели приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public delegate IApplicationModel ApplicationModelFactoryDelegate(
    	[NotNullAttribute] IApplicationCatalog applicationCatalog,
    	[NotNullAttribute] ApplicationPackage applicationPackage
    )
VB __Копировать
    <NotNullAttribute>
    Public Delegate Function ApplicationModelFactoryDelegate ( 
    	<NotNullAttribute> applicationCatalog As IApplicationCatalog,
    	<NotNullAttribute> applicationPackage As ApplicationPackage
    ) As IApplicationModel
C++ __Копировать
    [NotNullAttribute]
    public delegate IApplicationModel^ ApplicationModelFactoryDelegate(
    	[NotNullAttribute] IApplicationCatalog^ applicationCatalog, 
    	[NotNullAttribute] ApplicationPackage^ applicationPackage
    )
F# __Копировать
     [<NotNullAttribute>]
    type ApplicationModelFactoryDelegate = 
        delegate of 
            [<NotNullAttribute>] applicationCatalog : IApplicationCatalog * 
            [<NotNullAttribute>] applicationPackage : ApplicationPackage -> IApplicationModel
#### Параметры
applicationCatalog
[IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)
     Каталог приложений 
applicationPackage
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Пакет приложения 
#### Возвращаемое значение
[IApplicationModel](T_Tessa_Applications_IApplicationModel.htm)  
Возвращает модель приложения
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
