# LocalizationManager - класс
##  __Definition
 **Пространство имён:** [Tessa.Localization](N_Tessa_Localization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class LocalizationManager
VB __Копировать
     Public MustInherit Class LocalizationManager
C++ __Копировать
     public ref class LocalizationManager abstract
F# __Копировать
     [<AbstractClassAttribute>]
    type LocalizationManager = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LocalizationManager
Derived
[Tessa.Localization.ClientLocalizationManager](T_Tessa_Localization_ClientLocalizationManager.htm)
[Tessa.Web.Services.LocalizationManagerServer](T_Tessa_Web_Services_LocalizationManagerServer.htm)
##  __Конструкторы
[LocalizationManager](M_Tessa_Localization_LocalizationManager__ctor.htm)|
Инициализирует новый экземпляр класса LocalizationManager  
---|---  
##  __Свойства
[CurrentCulture](P_Tessa_Localization_LocalizationManager_CurrentCulture.htm)|
Региональные настройки для текущего потока. При получении значения не равен
null.  
---|---  
[CurrentUICulture](P_Tessa_Localization_LocalizationManager_CurrentUICulture.htm)|
Язык интерфейса для текущего потока. При получении значения не равен null.  
[DefaultCulture](P_Tessa_Localization_LocalizationManager_DefaultCulture.htm)|
Региональные настройки по умолчанию, доступные для всех потоков.  
[DefaultUICulture](P_Tessa_Localization_LocalizationManager_DefaultUICulture.htm)|
Язык интерфейса по умолчанию, доступный для всех потоков.  
[EnglishCultureInfo](P_Tessa_Localization_LocalizationManager_EnglishCultureInfo.htm)|
Английский язык локализации.  
[Service](P_Tessa_Localization_LocalizationManager_Service.htm)|  Используемый
сервис локализации.  
[UserDefaultUICulture](P_Tessa_Localization_LocalizationManager_UserDefaultUICulture.htm)|
Культура по умолчанию, используемая в операционной системе для отображения UI
текущего пользователя.  
## __Методы
[CreateScope(CultureInfo)](M_Tessa_Localization_LocalizationManager_CreateScope.htm)|  
---|---  
[CreateScope(CultureInfo,
CultureInfo)](M_Tessa_Localization_LocalizationManager_CreateScope_1.htm)|  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[EscapeIfLocalizationString](M_Tessa_Localization_LocalizationManager_EscapeIfLocalizationString.htm)|  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Format(String)](M_Tessa_Localization_LocalizationManager_Format.htm)|  
[Format(String,
CultureInfo)](M_Tessa_Localization_LocalizationManager_Format_1.htm)|  
[Format(String,
Object)](M_Tessa_Localization_LocalizationManager_Format_9.htm)|  
[Format(String,
Object[])](M_Tessa_Localization_LocalizationManager_Format_12.htm)|  
[Format(String,
String)](M_Tessa_Localization_LocalizationManager_Format_13.htm)|  
[Format(String, CultureInfo,
Object)](M_Tessa_Localization_LocalizationManager_Format_2.htm)|  
[Format(String, CultureInfo,
Object[])](M_Tessa_Localization_LocalizationManager_Format_5.htm)|  
[Format(String, CultureInfo,
String)](M_Tessa_Localization_LocalizationManager_Format_6.htm)|  
[Format(String, Object,
Object)](M_Tessa_Localization_LocalizationManager_Format_10.htm)|  
[Format(String, String,
String)](M_Tessa_Localization_LocalizationManager_Format_14.htm)|  
[Format(String, CultureInfo, Object,
Object)](M_Tessa_Localization_LocalizationManager_Format_3.htm)|  
[Format(String, CultureInfo, String,
String)](M_Tessa_Localization_LocalizationManager_Format_7.htm)|  
[Format(String, Object, Object,
Object)](M_Tessa_Localization_LocalizationManager_Format_11.htm)|  
[Format(String, String, String,
String)](M_Tessa_Localization_LocalizationManager_Format_15.htm)|  
[Format(String, CultureInfo, Object, Object,
Object)](M_Tessa_Localization_LocalizationManager_Format_4.htm)|  
[Format(String, CultureInfo, String, String,
String)](M_Tessa_Localization_LocalizationManager_Format_8.htm)|  
[GetAllStrings](M_Tessa_Localization_LocalizationManager_GetAllStrings.htm)|  
[GetAllStringsAsync](M_Tessa_Localization_LocalizationManager_GetAllStringsAsync.htm)|  
[GetEncoding](M_Tessa_Localization_LocalizationManager_GetEncoding.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetNameOrValue(String)](M_Tessa_Localization_LocalizationManager_GetNameOrValue.htm)|  
[GetNameOrValue(String,
CultureInfo)](M_Tessa_Localization_LocalizationManager_GetNameOrValue_1.htm)|  
[GetString(String)](M_Tessa_Localization_LocalizationManager_GetString.htm)|  
[GetString(String,
CultureInfo)](M_Tessa_Localization_LocalizationManager_GetString_1.htm)|  
[GetStringAsync(String,
CancellationToken)](M_Tessa_Localization_LocalizationManager_GetStringAsync_1.htm)|  
[GetStringAsync(String, CultureInfo,
CancellationToken)](M_Tessa_Localization_LocalizationManager_GetStringAsync.htm)|  
[GetSystemLanguageName](M_Tessa_Localization_LocalizationManager_GetSystemLanguageName.htm)|
Определяет язык локализации системы, доступный для текущего пользователя, и
возвращает его, либо английский язык, если язык системы не удалось определить.
По возвращёной строке можно получить культуру, вызвав метод
[GetCultureInfo(String)](https://learn.microsoft.com/dotnet/api/system.globalization.cultureinfo.getcultureinfo#system-
globalization-cultureinfo-getcultureinfo\(system-string\)).  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitializeAsync(ILocalizationService)](M_Tessa_Localization_LocalizationManager_InitializeAsync_1.htm)|  
[InitializeAsync(LocalizationManager)](M_Tessa_Localization_LocalizationManager_InitializeAsync_2.htm)|  
[InitializeAsync(ResourceManager)](M_Tessa_Localization_LocalizationManager_InitializeAsync.htm)|  
[InitializeByDefaultAsync](M_Tessa_Localization_LocalizationManager_InitializeByDefaultAsync.htm)|  
[InitializeDefaultLocalizationAsync(Boolean,
ResourceManager[])](M_Tessa_Localization_LocalizationManager_InitializeDefaultLocalizationAsync.htm)|
Инициализирует локализацию по умолчанию, т.е. до того, как настройки
локализации будут загружены. В качестве культуры по умолчанию используется
язык системы.  
[InitializeDefaultLocalizationAsync(Boolean,
ILocalizationService[])](M_Tessa_Localization_LocalizationManager_InitializeDefaultLocalizationAsync_1.htm)|
Инициализирует локализацию по умолчанию, т.е. до того, как настройки
локализации будут загружены. В качестве культуры по умолчанию используется
язык системы.  
[InvalidateCacheAsync](M_Tessa_Localization_LocalizationManager_InvalidateCacheAsync.htm)|  
[InvalidateUserDefaultUICulture](M_Tessa_Localization_LocalizationManager_InvalidateUserDefaultUICulture.htm)|
Сбрасывает культуру по умолчанию, используемую в операционной системе для
отображения UI текущего пользователя
[UserDefaultUICulture](P_Tessa_Localization_LocalizationManager_UserDefaultUICulture.htm).  
[Localize(String)](M_Tessa_Localization_LocalizationManager_Localize.htm)|  
[Localize(String,
CultureInfo)](M_Tessa_Localization_LocalizationManager_Localize_1.htm)|  
[LocalizeAndEscapeFormat(String)](M_Tessa_Localization_LocalizationManager_LocalizeAndEscapeFormat.htm)|  
[LocalizeAndEscapeFormat(String,
CultureInfo)](M_Tessa_Localization_LocalizationManager_LocalizeAndEscapeFormat_1.htm)|  
[LocalizeAndEscapeFormatAsync(String,
CancellationToken)](M_Tessa_Localization_LocalizationManager_LocalizeAndEscapeFormatAsync_1.htm)|  
[LocalizeAndEscapeFormatAsync(String, CultureInfo,
CancellationToken)](M_Tessa_Localization_LocalizationManager_LocalizeAndEscapeFormatAsync.htm)|  
[LocalizeAsync(String,
CancellationToken)](M_Tessa_Localization_LocalizationManager_LocalizeAsync_1.htm)|  
[LocalizeAsync(String, CultureInfo,
CancellationToken)](M_Tessa_Localization_LocalizationManager_LocalizeAsync.htm)|  
[LocalizeOrGetName(String)](M_Tessa_Localization_LocalizationManager_LocalizeOrGetName.htm)|  
[LocalizeOrGetName(String,
CultureInfo)](M_Tessa_Localization_LocalizationManager_LocalizeOrGetName_1.htm)|  
[LocalizeOrGetNameAsync(String,
CancellationToken)](M_Tessa_Localization_LocalizationManager_LocalizeOrGetNameAsync_1.htm)|  
[LocalizeOrGetNameAsync(String, CultureInfo,
CancellationToken)](M_Tessa_Localization_LocalizationManager_LocalizeOrGetNameAsync.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetEnglishLocalization](M_Tessa_Localization_LocalizationManager_SetEnglishLocalization.htm)|
Устанавливает английский язык в качестве языка локализации. Не изменяет
используемый сервис локализации.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetName(String)](M_Tessa_Localization_LocalizationManager_TryGetName.htm)|  
[TryGetName(String,
CultureInfo)](M_Tessa_Localization_LocalizationManager_TryGetName_1.htm)|  
[TryGetString(String)](M_Tessa_Localization_LocalizationManager_TryGetString.htm)|  
[TryGetString(String,
CultureInfo)](M_Tessa_Localization_LocalizationManager_TryGetString_1.htm)|  
[TryGetStringAsync(String,
CancellationToken)](M_Tessa_Localization_LocalizationManager_TryGetStringAsync_1.htm)|  
[TryGetStringAsync(String, CultureInfo,
CancellationToken)](M_Tessa_Localization_LocalizationManager_TryGetStringAsync.htm)|  
[TryLocalize(String)](M_Tessa_Localization_LocalizationManager_TryLocalize.htm)|  
[TryLocalize(String,
CultureInfo)](M_Tessa_Localization_LocalizationManager_TryLocalize_1.htm)|  
[TryLocalizeAsync(String,
CancellationToken)](M_Tessa_Localization_LocalizationManager_TryLocalizeAsync_1.htm)|  
[TryLocalizeAsync(String, CultureInfo,
CancellationToken)](M_Tessa_Localization_LocalizationManager_TryLocalizeAsync.htm)|  
## __События
[CurrentCultureChanged](E_Tessa_Localization_LocalizationManager_CurrentCultureChanged.htm)|
Событие, возникающее при изменении региональных настроек
[CurrentCulture](P_Tessa_Localization_LocalizationManager_CurrentCulture.htm).  
---|---  
[CurrentUICultureChanged](E_Tessa_Localization_LocalizationManager_CurrentUICultureChanged.htm)|
Событие, возникающее при изменении языка интерфейса
[CurrentUICulture](P_Tessa_Localization_LocalizationManager_CurrentUICulture.htm).  
[DefaultCultureChanged](E_Tessa_Localization_LocalizationManager_DefaultCultureChanged.htm)|
Событие, возникающее при изменении языка интерфейса
[DefaultCulture](P_Tessa_Localization_LocalizationManager_DefaultCulture.htm).  
[DefaultUICultureChanged](E_Tessa_Localization_LocalizationManager_DefaultUICultureChanged.htm)|
Событие, возникающее при изменении языка интерфейса
[DefaultUICulture](P_Tessa_Localization_LocalizationManager_DefaultUICulture.htm).  
## __Поля
[EnglishLanguageCode](F_Tessa_Localization_LocalizationManager_EnglishLanguageCode.htm)|  
---|---  
[RussianLanguageCode](F_Tessa_Localization_LocalizationManager_RussianLanguageCode.htm)|  
## __Методы расширения
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
[Tessa.Localization - пространство имён](N_Tessa_Localization.htm)
