# IRegistrator - интерфейс
Интерфейс, реализуемый в объектах регистраторов. Помимо интерфейса также
требуется указать атрибут
[RegistratorAttribute](T_Tessa_Extensions_RegistratorAttribute.htm).
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IRegistrator : ISealable
VB __Копировать
     Public Interface IRegistrator
    	Inherits ISealable
C++ __Копировать
     public interface class IRegistrator : ISealable
F# __Копировать
     type IRegistrator = 
        interface
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[InstanceName](P_Tessa_Extensions_IRegistrator_InstanceName.htm)|  Имя
экземпляра сервера или null, если регистрация выполняется на клиенте.  
---|---  
[IsPlatform](P_Tessa_Extensions_IRegistrator_IsPlatform.htm)|  Признак того,
что объект выполняет регистрацию платформенных расширений. Этот признак
используется системой, не рекомендуется его устанавливать.  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[SessionType](P_Tessa_Extensions_IRegistrator_SessionType.htm)| Тип сессии.  
[Tag](P_Tessa_Extensions_IRegistrator_Tag.htm)|  Флаговое перечисление с
тегами регистратора, которые ограничивают область его использования. По
умолчанию используются теги [Tessa.Extensions.RegistratorTag.Default].  
[UnityContainer](P_Tessa_Extensions_IRegistrator_UnityContainer.htm)|
Контейнер Unity, в котором выполняется регистрация. Гарантированно не равен
null.  
## __Методы
[FinalizeRegistration](M_Tessa_Extensions_IRegistrator_FinalizeRegistration.htm)|
Завершает регистрацию. В этом методе рекомендуется получить зависимости из
Unity и выполнить их настройку.  
---|---  
[InitializeExtensions](M_Tessa_Extensions_IRegistrator_InitializeExtensions.htm)|
Выполняет инициализацию заданного контейнера расширений. Рекомендуется не
выполнять регистрацию Unity в этом объекте.  
[InitializeRegistration](M_Tessa_Extensions_IRegistrator_InitializeRegistration.htm)|
Инициализирует регистрацию. В этом методе рекомендуется зарегистрировать
зависимости в Unity, которые необходимы уже на момент регистрации расширений.  
[RegisterExtensions](M_Tessa_Extensions_IRegistrator_RegisterExtensions.htm)|
Выполняет регистрацию расширений. Рекомендуется не выполнять регистрацию Unity
в этом объекте.  
[RegisterUnity](M_Tessa_Extensions_IRegistrator_RegisterUnity.htm)| Выполняет
регистрацию объектов расширений и их зависимостей в контейнере Unity.  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
