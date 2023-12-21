# TessaServerConfigFlags - перечисление
Перечисление параметров загрузки настроек сервера TESSA
[TessaServerSettings](T_Tessa_Platform_TessaServerSettings.htm) из файла
конфигурации.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum TessaServerConfigFlags
VB __Копировать
    <FlagsAttribute>
    Public Enumeration TessaServerConfigFlags
C++ __Копировать
    [FlagsAttribute]
    public enum class TessaServerConfigFlags
F# __Копировать
     [<FlagsAttribute>]
    type TessaServerConfigFlags
##  __Члены
None| 0|  Параметры не заданы.  
---|---|---  
OptionalLicensePath| 1|  Ключ "LicenseFile" является опциональным. Если он
отсутствут в файле конфигурации или файл лицензии не найден, то свойству
[LicensePath](P_Tessa_Platform_TessaServerSettings_LicensePath.htm)
присваивается значение по умолчанию.  
DefaultSignatureKey| 2|  Использовать значение по умолчанию для свойства
[SignatureKey](P_Tessa_Platform_ITessaServerSettings_SignatureKey.htm).  
DefaultCipherKey| 4|  Использовать значение по умолчанию для свойства
[CipherKey](P_Tessa_Platform_ITessaServerSettings_CipherKey.htm).  
TestDefaults| 7|  Параметры по умолчанию, используемые в тестах.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
