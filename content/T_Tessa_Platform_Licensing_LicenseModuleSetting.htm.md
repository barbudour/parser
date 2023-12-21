# LicenseModuleSetting - класс
Информация по одной из настроек модуля лицензии
[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm), используемая
в информации по типу модуля
[LicenseModuleType](T_Tessa_Platform_Licensing_LicenseModuleType.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class LicenseModuleSetting : ICloneable
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class LicenseModuleSetting
    	Implements ICloneable
C++ __Копировать
    [SerializableAttribute]
    public ref class LicenseModuleSetting sealed : ICloneable
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type LicenseModuleSetting = 
        class
            interface ICloneable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LicenseModuleSetting
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable)
##  __Конструкторы
[LicenseModuleSetting](M_Tessa_Platform_Licensing_LicenseModuleSetting__ctor.htm)|
Инициализирует новый экземпляр класса LicenseModuleSetting  
---|---  
##  __Свойства
[Caption](P_Tessa_Platform_Licensing_LicenseModuleSetting_Caption.htm)|
Отображаемое пользователю название настройки.  
---|---  
[DefaultValue](P_Tessa_Platform_Licensing_LicenseModuleSetting_DefaultValue.htm)|
Значение по умолчанию, сериализованное в виде строки, или null, если
используется значение по умолчанию для типа
[Type](P_Tessa_Platform_Licensing_LicenseModuleSetting_Type.htm). Пустая
строка Empty преобразуется в значение null.  
[Description](P_Tessa_Platform_Licensing_LicenseModuleSetting_Description.htm)|
Описание настройки. В настоящий момент при редактировании модуля описание
выводится пользователю как всплывающая подсказка и только для типа настройки
[Boolean](T_Tessa_Platform_Licensing_LicenseModuleSettingType.htm). Пустая
строка Empty преобразуется в значение null.  
[Items](P_Tessa_Platform_Licensing_LicenseModuleSetting_Items.htm)|  Элементы
в объекте настройки модуля лицензии. Используются для указания значений,
которые можно выбрать для настройки-перечисления типа
[Enum](T_Tessa_Platform_Licensing_LicenseModuleSettingType.htm).  
[Key](P_Tessa_Platform_Licensing_LicenseModuleSetting_Key.htm)|  Ключ, по
которому настройка сохраняется в
[Settings](P_Tessa_Platform_Licensing_ILicenseModule_Settings.htm). Ключ
должен быть уникален для всех настроек в пределах одного типа модуля.  
[Tag](P_Tessa_Platform_Licensing_LicenseModuleSetting_Tag.htm)|
Дополнительный признак для настройки в модуле лицензии.  
[TagAttribute](P_Tessa_Platform_Licensing_LicenseModuleSetting_TagAttribute.htm)|
Дополнительный признак для настройки в модуле лицензии в виде строки для
сериализации.  
[Type](P_Tessa_Platform_Licensing_LicenseModuleSetting_Type.htm)|  Тип
редактируемой настройки, определяющий также тип данных в настройках модуля
[Settings](P_Tessa_Platform_Licensing_ILicenseModule_Settings.htm).  
## __Методы
[Clone](M_Tessa_Platform_Licensing_LicenseModuleSetting_Clone.htm)| Создаёт
полную копию объекта.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Repair](M_Tessa_Platform_Licensing_LicenseModuleSetting_Repair.htm)|
Исправляет объект. Рекомендуется использовать перед сериализацией. Если тип
настройки отличен от перечисления, то метод удаляет список элементов
[Items](P_Tessa_Platform_Licensing_LicenseModuleSetting_Items.htm).  
[ToString](M_Tessa_Platform_Licensing_LicenseModuleSetting_ToString.htm)|
Возвращает строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
