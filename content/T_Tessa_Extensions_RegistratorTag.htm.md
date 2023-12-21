# RegistratorTag - перечисление
Флаговое перечисление с тегами регистратора, которые ограничивают область его
использования.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum RegistratorTag
VB __Копировать
    <FlagsAttribute>
    Public Enumeration RegistratorTag
C++ __Копировать
    [FlagsAttribute]
    public enum class RegistratorTag
F# __Копировать
     [<FlagsAttribute>]
    type RegistratorTag
##  __Члены
None| 0|  Регистратор не будет использоваться.  
---|---|---  
Database| 1|  Регистратор будет использоваться при регистрации плагина или
консольной утилиты, использующей только подключение к базе данных, т.е.
вызывающий RegisterDatabase или RegisterDatabaseForPlugin.  
Client| 2|  Регистратор будет использоваться при регистрации клиента. Это
любые приложения, вызывающие RegisterClient. Такие расширения по умолчанию не
выполняются для менеджера приложений, используйте для этого флаг
AppManagerClient.  
ServerDefault| 4|  Регистратор будет использоваться при регистрации сервера по
умолчанию. Обычно это веб-сервис "tessa", вызывающий RegisterServer. Это как
веб-сервисы "tessa" и "web", так и серверные плагины, вызывающие
RegisterServer или RegisterServerForPlugin.  
ServerWeb| 8|  Регистратор будет использоваться при регистрации сервера для
web-клиента. Обычно это веб-сервис "web", вызывающий RegisterServer с
указанием этого тега.  
ServerPlugin| 16|  Регистратор будет использоваться при регистрации сервера
для серверных плагинов и standalone-приложений, вызывающих
RegisterServerForPlugin. Обычно это сервис Chronos.  
Server| 28|  Регистратор будет использоваться при регистрации любого сервера,
т.е. ServerDefault, ServerWeb или ServerPlugin.  
Default| 30|  По умолчанию регистратор будет вызван как для Server, так и для
Client, но не будет вызван для Database или ConsoleClient.  
ConsoleClient| 32|  Регистратор будет использоваться при регистрации клиента
для консольных приложений, которые инициализируют контейнер Unity без
зависимостей от Tessa.UI.dll.  
DefaultForClientAndConsole| 34|  Флаги по умолчанию для регистратора, который
выполняет регитрацию расширений, выполняемых на клиенте и в консольном
приложении. Как правило, это такие расширения, как метаинформация по типам
карточек
[ICardMetadataExtension](T_Tessa_Cards_Extensions_ICardMetadataExtension.htm).  
DefaultForRepair| 62|  Флаги по умолчанию для регистратора, который выполняет
регитрацию расширений, выполняемых на сервере, на клиенте, а также в
консольном приложении. Как правило, это такие расширения, как исправление
структуры карточки
[ICardRepairExtension](T_Tessa_Cards_Extensions_ICardRepairExtension.htm).  
AppManagerClient| 64|  Регистратор будет использоваться в менеджере
приложений, в котором по умолчанию не выполняются другие клиентские
расширения.  
## __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
