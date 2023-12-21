# CardHelper.GetSubContentDirectoryProvider - метод
Получает провайдер поддиректории для карточки на основании провайдера для
файла самой карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ISourceDirectoryProvider GetSubContentDirectoryProvider(
    	ISourceContentProvider cardFileProvider
    )
VB __Копировать
     Public Shared Function GetSubContentDirectoryProvider ( 
    	cardFileProvider As ISourceContentProvider
    ) As ISourceDirectoryProvider
C++ __Копировать
     public:
    static ISourceDirectoryProvider^ GetSubContentDirectoryProvider(
    	ISourceContentProvider^ cardFileProvider
    )
F# __Копировать
     static member GetSubContentDirectoryProvider : 
            cardFileProvider : ISourceContentProvider -> ISourceDirectoryProvider 
#### Параметры
cardFileProvider
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
    Провайдер файла карточки.
#### Возвращаемое значение
[ISourceDirectoryProvider](T_Tessa_Platform_SourceProviders_ISourceDirectoryProvider.htm)  
Провайдер поддиректории для карточки.
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
