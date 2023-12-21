# ApplicationHelper - класс
Вспомогательные методы для приложения.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ApplicationHelper
VB __Копировать
     Public NotInheritable Class ApplicationHelper
C++ __Копировать
     public ref class ApplicationHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ApplicationHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationHelper
##  __Свойства
[ApplicationIcon](P_Tessa_UI_ApplicationHelper_ApplicationIcon.htm)|  Иконка,
с которым приложение было опубликовано, или иконка, встроенная в сборку, если
приложение не было опубликовано, или стандартная иконка приложения, если
иконка отсутствует в сборке приложения.  
---|---  
[AssemblyIcon](P_Tessa_UI_ApplicationHelper_AssemblyIcon.htm)|  Иконка,
встроенная в сборку приложения, или стандартная иконка приложения, если иконка
не найдена.  
[CanSaveCredentials](P_Tessa_UI_ApplicationHelper_CanSaveCredentials.htm)|
Признак того, что возможно сохранение логина или пароля в Tessa Applications.
Если значение отсутствует, то логин и пароль сохранять нельзя, и уже
сохранённые логин/пароль также не могут быть использованы, всегда требуется
вводить их заново.  
[DefaultWallpaper](P_Tessa_UI_ApplicationHelper_DefaultWallpaper.htm)|  Путь к
фоновому изображению по умолчанию или null, если фоновое изображение по
умолчанию не указано.  
[DialogOwner](P_Tessa_UI_ApplicationHelper_DialogOwner.htm)|  Объект,
являющийся родительским для диалоговых окон, или null, если в качестве
родительского будет использоваться основное окно приложения. Для получения
значения используйте метод
[GetDialogOwner(Boolean)](M_Tessa_UI_ApplicationHelper_GetDialogOwner.htm).  
[LogoBackground](P_Tessa_UI_ApplicationHelper_LogoBackground.htm)|  Цвет фона
на экране загрузки или null, если используется стандартный цвет.  
[LogoForeground](P_Tessa_UI_ApplicationHelper_LogoForeground.htm)|  Цвет
текста на экране загрузки или null, если используется стандартный цвет.  
[LogoHideFrame](P_Tessa_UI_ApplicationHelper_LogoHideFrame.htm)|  Признак
того, что обрамление надо скрыть на экране загрузки. По умолчанию равен false.  
[LogoHideProgress](P_Tessa_UI_ApplicationHelper_LogoHideProgress.htm)|
Признак того, что прогресс бар надо скрыть на экране загрузки. По умолчанию
равен false.  
[LogoHideText](P_Tessa_UI_ApplicationHelper_LogoHideText.htm)|  Признак того,
что строку с текстом надо скрыть на экране загрузки. По умолчанию равен false.  
[LogoHideVersion](P_Tessa_UI_ApplicationHelper_LogoHideVersion.htm)|  Признак
того, что строку с версией надо скрыть на экране загрузки. По умолчанию равен
false.  
[LogoText](P_Tessa_UI_ApplicationHelper_LogoText.htm)|  Текст под логотипом на
экране загрузки или null, если текст не задан и следует использовать
стандартный текст. Строка "\n" заменяется на перевод строки.  
[MaxPreviewInstances](P_Tessa_UI_ApplicationHelper_MaxPreviewInstances.htm)|
Максимальное количество одновременно возможных экземпляров процессов для
просмотра файлов.  
[RemoteSession](P_Tessa_UI_ApplicationHelper_RemoteSession.htm)|  Возвращает
признак того, что приложение запущено в терминальной сессии, такой как RDP.
Позволяет отключить такие визуальные эффекты, как затемнение экрана.  
[SoftwareRendering](P_Tessa_UI_ApplicationHelper_SoftwareRendering.htm)|
Признак того, что отображение интерфейса в WPF не должно использовать
аппаратное ускорение, т.е. должен производиться программный рендеринг.  
[Title](P_Tessa_UI_ApplicationHelper_Title.htm)|  Заголовок окна приложения
или null, если используется стандартный заголовок.  
[UseFilePreview64Bit](P_Tessa_UI_ApplicationHelper_UseFilePreview64Bit.htm)|
Признак того, что предпросмотр файлов в 64-битном приложении должен
выполняться также средствами 64-битного обработчика предпросмотра. В таком
случае возможны некоторые проблемы предпросмотра средствами Microsoft Office.
Настройка не влияет на запуск приложений в 32-битном процессе (и на 32-битных
ОС).  
[WallpaperFolder](P_Tessa_UI_ApplicationHelper_WallpaperFolder.htm)|  Путь к
папке с доступными фоновыми изображениями (относительно файлов приложения) или
null, если используется папка по умолчанию wallpapers. Используйте совместно с
методом [GetExistentFolderPathList(String,
Assembly)](M_Tessa_Platform_Runtime_RuntimeHelper_GetExistentFolderPathList.htm).  
## __Методы
[ActivateMainWindow](M_Tessa_UI_ApplicationHelper_ActivateMainWindow.htm)|
Активирует главное окно приложения. Работает только в потоке UI, если у
приложения существует главное окно. Возвращает признак того, что главное окно
было успешно активировано.  
---|---  
[AppendClosingHandlersSync](M_Tessa_UI_ApplicationHelper_AppendClosingHandlersSync.htm)|
Добавляет к событиям
[ClosingBeforeCheck](F_Tessa_UI_ApplicationHelper_ClosingBeforeCheck.htm) и
[ClosingAfterCheck](F_Tessa_UI_ApplicationHelper_ClosingAfterCheck.htm)
заданные обработчики. Если такие обработчики уже были установлены, то они не
добавляются, но порядок обработчиков при этом может измениться. Вызовы метода
синхронизированы между потоками, т.е. гарантированно последовательны.  
[ApplySoftwareRenderingFromConfiguration](M_Tessa_UI_ApplicationHelper_ApplySoftwareRenderingFromConfiguration.htm)|
Применяет программный рендеринг (без аппаратного ускорения), если это
установлено в конфигурационном файле, т.е. установлена настройка
[SoftwareRendering](P_Tessa_UI_ApplicationHelper_SoftwareRendering.htm).  
[BringMainWindowIntoView](M_Tessa_UI_ApplicationHelper_BringMainWindowIntoView.htm)|
Переводит главное окно процесса на передний план. Не переводит фокус с других
приложений.  
[BringMainWindowToTop](M_Tessa_UI_ApplicationHelper_BringMainWindowToTop.htm)|
Выводит главное окно приложения на передний план. Если окно было свёрнуто, то
разворачивает его. Работает только в потоке UI, если у приложения существует
главное окно. Возвращает признак того, что главное окно было успешно выведено
на передний план.  
[CreateDefaultApplicationIcon](M_Tessa_UI_ApplicationHelper_CreateDefaultApplicationIcon.htm)|
Возвращает стандартную иконку, используемую для приложения в Windows.  
[CreateLauncherFromSettings](M_Tessa_UI_ApplicationHelper_CreateLauncherFromSettings.htm)|
Создаёт объект загрузочного экрана в соответствии с настройками из
конфигурационного файла app.json.  
[GetAssemblyIconDataFullSize](M_Tessa_UI_ApplicationHelper_GetAssemblyIconDataFullSize.htm)|
Возвращает массив байт, соответствующий иконке, встроенной в сборку, или же
стандартной иконке приложения, если в сборке отсутствует встроенная иконка. В
отличие от свойства
[AssemblyIcon](P_Tessa_UI_ApplicationHelper_AssemblyIcon.htm), возвращённые
данные по иконке не изменяются в размерах (что выполнялось в
[AssemblyIcon](P_Tessa_UI_ApplicationHelper_AssemblyIcon.htm) для отображения
в панели задач без артефактов).  
[GetAssemblyIconStream](M_Tessa_UI_ApplicationHelper_GetAssemblyIconStream.htm)|
Возвращает поток с данными иконки в формате PNG, которая встроена в заданную
сборку.  
[GetDialogOwner](M_Tessa_UI_ApplicationHelper_GetDialogOwner.htm)|  Метод для
получения текущего основного окна в соответствии со значением из свойства
[DialogOwner](P_Tessa_UI_ApplicationHelper_DialogOwner.htm). При этом не
вызывается обращение к потоку UI или связанным с ним свойствам.  
[GetLogoUri](M_Tessa_UI_ApplicationHelper_GetLogoUri.htm)|  Возвращает Uri к
логотипу, указанному в настройках приложения, или null, если должен быть
использован стандартный логотип. Рекомендуется использовать совместно с
методом [CreateLauncher(Uri, String, String, Boolean, Boolean, Boolean,
Nullable<Color>, Nullable<Color>)](M_Tessa_UI_TessaSplash_CreateLauncher.htm).  
[HandleDispatcherUnhandledException](M_Tessa_UI_ApplicationHelper_HandleDispatcherUnhandledException.htm)|
Выполняет обработку исключения для события
[DispatcherUnhandledException](https://learn.microsoft.com/dotnet/api/system.windows.application.dispatcherunhandledexception).  
[HandleDispatcherUnhandledExceptionWithSafeLocalization](M_Tessa_UI_ApplicationHelper_HandleDispatcherUnhandledExceptionWithSafeLocalization.htm)|
Выполняет обработку исключения для события
[DispatcherUnhandledException](https://learn.microsoft.com/dotnet/api/system.windows.application.dispatcherunhandledexception),
учитывая безопасную инициализацию локализации.  
[InitializeDescriptorAsync](M_Tessa_UI_ApplicationHelper_InitializeDescriptorAsync.htm)|
Выполняет инициализацию дескриптора приложения, посредством которого может
быть получена иконка
[ApplicationIcon](P_Tessa_UI_ApplicationHelper_ApplicationIcon.htm), а также
текущие настройки приложения.  
[PerformClosingCheckWithEventsAsync](M_Tessa_UI_ApplicationHelper_PerformClosingCheckWithEventsAsync.htm)|
Вызывает обработку событий контролируемого закрытия приложения с
использованием событий
[ClosingBeforeCheck](F_Tessa_UI_ApplicationHelper_ClosingBeforeCheck.htm) и
[ClosingAfterCheck](F_Tessa_UI_ApplicationHelper_ClosingAfterCheck.htm), и с
возможностью указать стандартную обработку закрытия defaultCheckFuncAsync.
Метод обрабатывает исключения, которые могут возникнуть в обработчиках события
или в функции defaultCheckFuncAsync, в этом случае исключение выводится
пользователю и закрытие отменяется. Возвращает признак того, что закрытие окна
подтверждено.  
[SetupAppContextSwitchesForWpf](M_Tessa_UI_ApplicationHelper_SetupAppContextSwitchesForWpf.htm)|
Устанавливает настройки
[AppContext](https://learn.microsoft.com/dotnet/api/system.appcontext) для
оптимального функционирования приложений WPF.  
[ShouldShowMessageInTaskBar](M_Tessa_UI_ApplicationHelper_ShouldShowMessageInTaskBar.htm)|
Возвращает признак того, что окно с сообщением должно быть выведено в панели
задач. Если метод вызван в потоке UI и главное окно приложения отсутствует или
ещё не создано, или если приложение WPF ещё не инициализировано, то возвращает
true. В других случаях возвращает false.  
[TryExtractIconFromFile](M_Tessa_UI_ApplicationHelper_TryExtractIconFromFile.htm)|
Извлекает иконку, встроенную в заданный файл, и возвращает её в виде объекта
[Icon](https://learn.microsoft.com/dotnet/api/system.drawing.icon). Возвращает
null, если извлечь иконку не удалось.  
[TryGetRecommendedIconDataFromIcoFileAsync](M_Tessa_UI_ApplicationHelper_TryGetRecommendedIconDataFromIcoFileAsync.htm)|
Возвращает данные для рекомендуемой иконки, полученной из заданного файла
формата .ICO, или null, если данные получить не удалось. Метод не выбрасывает
исключений, ошибки логируются и возвращаются как null.  
## __Поля
[ClosingAfterCheck](F_Tessa_UI_ApplicationHelper_ClosingAfterCheck.htm)|
Событие по закрытию окна приложения, выполняемое после того, как пользователь
был проинформирован о необходимости сохранить изменения во вкладках и
подтвердил закрытие, несмотря на это. Если обработчики события
[ClosingBeforeCheck](F_Tessa_UI_ApplicationHelper_ClosingBeforeCheck.htm) уже
отменили закрытие, установив e.Cancel = true, или обработчики вызвали
исключение, то это событие не будет вызвано, а закрытие будет отменено. Если
пользователь подтвердил закрытие или обработчики события
[ClosingBeforeCheck](F_Tessa_UI_ApplicationHelper_ClosingBeforeCheck.htm)
установили e.ForceClosing = true, то это событие будет вызвано, но в этом
случае будет установлено e.Cancel = true в аргументах события.  
---|---  
[ClosingBeforeCheck](F_Tessa_UI_ApplicationHelper_ClosingBeforeCheck.htm)|
Событие по закрытию окна приложения, выполняемое до того, как будут сделаны
проверки по умолчанию, и пользователь будет проинформирован о необходимости
сохранить изменения во вкладках.  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
