# CardStoreAsyncResponse.FileProgress - свойство
Прогресс операции, вычисляемый как отношение суммарного количества уже
загруженных байт, относящихся к файлам, к суммарному размеру всех файлов,
которые требуется загрузить. Не учитывает размеры заголовка и запроса на
сохранение карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public double FileProgress { get; }
VB __Копировать
     Public ReadOnly Property FileProgress As Double
    	Get
C++ __Копировать
     public:
    virtual property double FileProgress {
    	double get () sealed;
    }
F# __Копировать
     abstract FileProgress : float with get
    override FileProgress : float with get
#### Значение свойства
[Double](https://learn.microsoft.com/dotnet/api/system.double)
#### Реализации
[ICardStoreAsyncResponse.FileProgress](P_Tessa_Cards_ICardStoreAsyncResponse_FileProgress.htm)  
##  __См. также
#### Ссылки
[CardStoreAsyncResponse - ](T_Tessa_Cards_CardStoreAsyncResponse.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
