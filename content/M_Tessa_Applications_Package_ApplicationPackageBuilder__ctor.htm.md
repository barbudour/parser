# ApplicationPackageBuilder - конструктор
Initializes a new instance of the
[ApplicationPackageBuilder](T_Tessa_Applications_Package_ApplicationPackageBuilder.htm)
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationPackageBuilder(
    	[NotNullAttribute] IPackageBinderFactory binderFactory
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> binderFactory As IPackageBinderFactory
    )
C++ __Копировать
     public:
    ApplicationPackageBuilder(
    	[NotNullAttribute] IPackageBinderFactory^ binderFactory
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] binderFactory : IPackageBinderFactory -> ApplicationPackageBuilder
#### Параметры
binderFactory
[IPackageBinderFactory](T_Tessa_Applications_Package_IPackageBinderFactory.htm)
     Предоставляет доступ к объектам осуществляющим формирование пакета приложения 
## __См. также
#### Ссылки
[ApplicationPackageBuilder -
](T_Tessa_Applications_Package_ApplicationPackageBuilder.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
