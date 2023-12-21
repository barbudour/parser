# RegistratorHelper - класс
Вспомогательные средства для выполнения регистрации, используя найденные
объекты.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class RegistratorHelper
VB __Копировать
     Public NotInheritable Class RegistratorHelper
C++ __Копировать
     public ref class RegistratorHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type RegistratorHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RegistratorHelper
##  __Методы
[CreateFinder](M_Tessa_Extensions_RegistratorHelper_CreateFinder.htm)|
Создаёт объект, позволяющий осуществлять поиск типов
[IRegistrator](T_Tessa_Extensions_IRegistrator.htm) в указанном каталоге со
сборками.  
---|---  
[Execute](M_Tessa_Extensions_RegistratorHelper_Execute.htm)|  Выполняет
регистрацию расширений и их зависимостей, используя заданный объект
[IFinder<T>](T_Tessa_Platform_Composition_IFinder_1.htm) для поиска и создания
регистраций.  
[FindAndExecute](M_Tessa_Extensions_RegistratorHelper_FindAndExecute.htm)|
Выполняет поиск и исполнение регистраторов расширений в папке приложения для
заданного типа сессии, который определяет сборки расширений платформы.  
## __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
